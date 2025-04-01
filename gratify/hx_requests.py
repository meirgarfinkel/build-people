from django.urls import reverse
from hx_requests.hx_requests import BaseHxRequest, FormHxRequest
from django.core.mail import send_mail
from django.contrib import messages
from gratify.forms import CreateRecognitionForm
from gratify.models import EmployeeInvite
from users.forms import UpdateUserForm
from django.utils.text import slugify


class AddEmployeeEmail(BaseHxRequest):
    name = "add_employee"
    GET_block = "new_employee_emails"

    def get_context_data(self, **kwargs) -> dict:
        email = self.request.GET.get("email")  # New email
        existing_emails = self.request.GET.get("employees_list", "").split(",")  # Previous emails

        # Remove empty strings and add the new email
        all_emails = list(dict.fromkeys([e.strip() for e in existing_emails if e] + ([email] if email else [])))

        context = {"new_emails": all_emails}
        return context


class SendEmployeeInvites(BaseHxRequest):
    name = "send_employee_invites"
    redirect = reverse("gratify:home")

    def post(self, request, *args, **kwargs):
        company = request.user.company
        email_list = self.request.POST.get("employees_list", "").split(",")

        for email in email_list:
            self.create_and_send_invite(company, email)
        return super().post(request, *args, **kwargs)
    
    def create_and_send_invite(self, company, email):
        invite = EmployeeInvite.objects.create(company=company, email=email)
        invite_link = f"http://localhost:8000{reverse('users:employee_signup', args=[invite.token])}"

        send_mail(
            subject="You're invited to join our company!",
            message=f"Click the link to sign up: {invite_link}",
            from_email="no-reply@yourdomain.com",
            recipient_list=[email],
        )


class ToggleHeart(BaseHxRequest):
    name = "toggle_heart"
    POST_template = "gratify/partials/heart_button.html"
    
    def get_context_on_POST(self, **kwargs):
        context = super().get_context_on_POST(**kwargs)
        recognition = self.hx_object
        user = self.request.user

        # Toggle heart status
        if kwargs.get("hearted"):
            recognition.hearts.remove(user)
        else:
            recognition.hearts.add(user)

        # hearted_by_user = recognition.hearts.filter(id=user.id).exists()
        recognition.refresh_from_db()
        recognition.hearted_by_user = recognition.hearts.filter(id=user.id).exists()

        context.update({"recognition": recognition})
        return context


class AddComment(BaseHxRequest):
    name = "add_comment"
    POST_template = "gratify/partials/recognitions_list.html"
    
    def get_context_on_POST(self, **kwargs):
        context = super().get_context_on_POST(**kwargs)
        recognition = self.hx_object
        user = self.request.user

        comment_text = self.request.POST.get("content")

        if comment_text:
            recognition.comments.create(user=user, content=comment_text)
            recognition.refresh_from_db()

        context.update({
            "recognition": recognition,
            "open": True,
        })
        return context


class CreateRecognition(FormHxRequest):
    name = "create_recognition"
    form_class = CreateRecognitionForm
    GET_template = "gratify/partials/recognition_form.html"
    POST_template = "gratify/partials/recognition_form.html"

    def form_valid(self, **kwargs) -> str:
        recognition = self.form.save(commit=False)
        recognition.created_by = self.request.user
        recognition.save()
        self.form.save_m2m()

        messages.success(self.request, "Success!")

        return self._get_response(
            template="gratify/partials/recognition_card.html",
            context={"recognition": recognition},
            **kwargs
        )

    def form_invalid(self, **kwargs) -> str:
        messages.error(self.request, "Failed to create recognition. Please correct the errors below.")
        response = super().form_invalid(**kwargs)
        response.headers["HX-Reswap"] = "innerHTML"
        return response


class UserForm(BaseHxRequest):
    name = "user_form"
    GET_template = "users/partials/user_form.html"
    GET_block = "content"


class UpdateUser(FormHxRequest):
    name = "update_user"
    form_class = UpdateUserForm
    GET_template = "users/partials/user_form.html"
    redirect = reverse("gratify:profile")

    def form_valid(self, **kwargs) -> str:
        user = self.request.user
        cleaned_data = self.form.cleaned_data
        # Only update fields that changed
        user.first_name = cleaned_data["first_name"]
        user.last_name = cleaned_data["last_name"]
        user.email = cleaned_data["email"]

        # Automatically update username
        user.username = slugify(f"{user.first_name} {user.last_name}")
        user.save(update_fields=["first_name", "last_name", "email", "username"])

        messages.success(self.request, self.get_success_message(**kwargs))
        return self._get_response(**kwargs)
    
    def form_invalid(self, **kwargs) -> str:
        self.is_post_request = False
        response = super().form_invalid(**kwargs)
        response.headers["HX-Reswap"] = "innerHTML"
        return response
