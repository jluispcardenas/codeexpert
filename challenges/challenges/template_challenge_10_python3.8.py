import json

[USER_FUNCTION]

def lambda_handler(event, context):
    
    parameters = [3,120,200,0,4000]
    expected = [0,28,49,0,999]

    result = {}

    test_passed = 0
    for i in range(len(parameters)):
        ret = Solution().trailingZeroes(parameters[i])
        if ret != expected[i]:
            return {'errorType': 'WrongAnswer', 'errorMessage': 'Error value: ' + str(parameters[i])}
        test_passed += 1

    result = {'status': 200, 'msg': 'Test passed: ' + str(test_passed)}

    return result
