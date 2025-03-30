from django.urls import reverse
from hx_requests.hx_requests import BaseHxRequest
from django.core.mail import send_mail

from gratify.models import EmployeeInvite


class AddEmployeeEmail(BaseHxRequest):
    name = "add_employee"
    GET_block = "new_employee_emails"

    def get_context_data(self, **kwargs) -> dict:
        email = self.request.GET.get("email")  # New email
        existing_emails = self.request.GET.get("employee_list", "").split(",")  # Previous emails

        # Remove empty strings and add the new email
        all_emails = list(dict.fromkeys([e.strip() for e in existing_emails if e] + ([email] if email else [])))

        context = {"new_emails": all_emails}
        return context


class SendEmployeeInvites(BaseHxRequest):
    name = "send_employee_invites"
    redirect = reverse("gratify:home")

    def post(self, request, *args, **kwargs):
        company = request.user.company
        email_list = self.request.POST.get("employee_list", "").split(",")

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

        context.update({
            "recognition": recognition,
            "user": user,
        })
        return context
