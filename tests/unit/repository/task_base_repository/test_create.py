from unittest.mock import MagicMock, patch

from faker import Faker

fake = Faker()

@patch("src.repositories.tasks.base.Task",)
def test_create_success(mock_task_class, task_base_repository):
    repository = task_base_repository
    repository.save = MagicMock()

    mock_instance = mock_task_class.return_value

    repository.create(name=fake.sentence(), deadline=fake.date_time())
    repository.save.assert_called_once_with(mock_instance)
