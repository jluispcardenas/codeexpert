import json

[USER_FUNCTION]

def lambda_handler(event, context):
    
    parameters = ["()", "()[]{}", "(]", "([)]", "{[]}"]
    expected = [True, True, False, False, True]

    result = {}

    test_passed = 0
    for i in range(len(parameters)):
        ret = Solution().isValid(parameters[i])
        if ret != expected[i]:
            return {'errorType': 'WrongAnswer', 'errorMessage': 'Error value: ' + str(parameters[i])}
        test_passed += 1

    result = {'status': 200, 'msg': 'Test passed: ' + str(test_passed)}

    return result
