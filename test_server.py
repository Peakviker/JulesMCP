import server
import json
import os

def test_analyze_repository():
    result = server.analyze_repository(".")
    data = json.loads(result)
    assert ".py" in data
    assert ".md" in data
    print("test_analyze_repository passed")

def test_get_system_info():
    result = server.get_system_info()
    data = json.loads(result)
    assert "platform" in data
    assert "python_version" in data
    print("test_get_system_info passed")

def test_manage_tasks():
    # Clear first
    server.manage_tasks("clear")

    # Add
    server.manage_tasks("add", "test task")
    result = server.manage_tasks("list")
    data = json.loads(result)
    assert len(data) == 1
    assert data[0]["task"] == "test task"

    # Clear again
    server.manage_tasks("clear")
    result = server.manage_tasks("list")
    assert result == "No tasks found."
    print("test_manage_tasks passed")

if __name__ == "__main__":
    test_analyze_repository()
    test_get_system_info()
    test_manage_tasks()
    print("All tests passed!")
