import json

[USER_FUNCTION]

def lambda_handler(event, context):
    
    parameters = [19, 1, 102, 7, 104]
    expected = [True, True, False, True, False]

    result = {}

    test_passed = 0
    for i in range(len(parameters)):
        ret = Solution().isHappy(parameters[i])
        if ret != expected[i]:
            return {'errorType': 'WrongAnswer', 'errorMessage': 'Error value: ' + str(expected[i])}
        test_passed += 1

    result = {'status': 200, 'msg': 'Test passed: ' + str(test_passed)}

    return result
