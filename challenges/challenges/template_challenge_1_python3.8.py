import json

[USER_FUNCTION]

def lambda_handler(event, context):
    
    parameters = [38, 102, 1052, 1, 10234]
    expected = [2, 3, 8, 1, 1]

    result = {}

    test_passed = 0
    for i in range(len(parameters)):
        ret = Solution().addDigits(parameters[i])
        if ret != expected[i]:
            return {'errorType': 'WrongAnswer', 'errorMessage': 'Error value: ' + str(parameters[i])}
        test_passed += 1

    result = {'status': 200, 'msg': 'Test passed: ' + str(test_passed)}

    return result
