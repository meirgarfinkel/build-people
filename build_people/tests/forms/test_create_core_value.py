import pytest
from build_people.forms import CreateCoreValue
from build_people.models import CoreValue

@pytest.mark.django_db
class TestCreateCoreValueForm:
    def test_valid_core_value_creation(self):
        form = CreateCoreValue(data={"name": "Teamwork"})
        assert form.is_valid()
        instance = form.save()
        assert instance.name == "teamwork"  # because form clean_name lowercases

    def test_duplicate_core_value_fails(self):
        # Pre-create an existing core value
        CoreValue.objects.create(name="teamwork")
        form = CreateCoreValue(data={"name": "TEAMWORK"})  # different casing
        assert not form.is_valid()
        assert "name" in form.errors
        assert "already exists" in form.errors["name"][0]

    def test_whitespace_and_case_normalization(self):
        CoreValue.objects.create(name="innovation")
        form = CreateCoreValue(data={"name": "  Innovation  "})
        assert not form.is_valid()
        assert "name" in form.errors
