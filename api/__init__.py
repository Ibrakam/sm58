def result_message(result):
    if result:
        return {"status": 1, "mesasge": result}
    return {"status": 0, "message": result}
