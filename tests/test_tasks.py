from datetime import date

import pytest

from app.tasks import TaskManager


def make_manager():
    manager = TaskManager()
    manager.add_task("Agile Assignment 8", "Agile Methodology", date(2026, 10, 25))
    manager.add_task("DBMS Lab", "DBMS", date(2026, 10, 10))
    return manager


def test_add_task_assigns_ids():
    manager = make_manager()
    assert manager.get_task(1).title == "Agile Assignment 8"
    assert manager.get_task(2).task_id == 2


def test_empty_title_is_rejected():
    manager = TaskManager()
    with pytest.raises(ValueError):
        manager.add_task("   ", "AM", date(2026, 10, 25))


def test_complete_task_marks_done():
    manager = make_manager()
    assert manager.complete_task(1).done is True
    assert len(manager.pending_tasks()) == 1


def test_complete_unknown_task_raises():
    manager = make_manager()
    with pytest.raises(KeyError):
        manager.complete_task(99)


def test_overdue_tasks():
    manager = make_manager()
    overdue = manager.overdue_tasks(date(2026, 10, 18))
    assert [t.title for t in overdue] == ["DBMS Lab"]


def test_progress_percent():
    manager = make_manager()
    assert manager.progress_percent() == 0.0
    manager.complete_task(1)
    assert manager.progress_percent() == 60.0


def test_progress_with_no_tasks():
    assert TaskManager().progress_percent() == 0.0
