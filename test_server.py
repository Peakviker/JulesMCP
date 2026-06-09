import server
import json
import os

def test_objectives():
    if os.path.exists("objective.json"): os.remove("objective.json")
    server.set_objective("Build the future")
    res = server.get_current_objective()
    data = json.loads(res)
    assert data["objective"] == "Build the future"
    print("test_objectives passed")

def test_events():
    if os.path.exists("events.json"): os.remove("events.json")
    server.emit_event("milestone", "First milestone reached")
    res = server.get_recent_events()
    data = json.loads(res)
    assert len(data) == 1
    assert data[0]["type"] == "milestone"
    print("test_events passed")

def test_manage_tasks_with_assignment():
    server.manage_tasks("clear")
    add_result = server.manage_tasks("add", "Write code", assigned_to="Jules")
    assert "Assigned to: Jules" in add_result

    list_result = server.manage_tasks("list")
    tasks = json.loads(list_result)
    assert tasks[0]["assigned_to"] == "Jules"

    server.manage_tasks("update", task_id=1, status="completed", assigned_to="Hermes")
    details = json.loads(server.get_task_details(1))
    assert details["status"] == "completed"
    assert details["assigned_to"] == "Hermes"
    print("test_manage_tasks_with_assignment passed")

def test_basic_tools():
    assert "platform" in json.loads(server.get_system_info())
    assert ".py" in json.loads(server.analyze_repository("."))
    print("test_basic_tools passed")

if __name__ == "__main__":
    test_objectives()
    test_events()
    test_manage_tasks_with_assignment()
    test_basic_tools()
    print("All tests passed!")
