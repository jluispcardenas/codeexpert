import json

[USER_FUNCTION]

def lambda_handler(event, context):
    
    parameters = [[1,3,4,2,2], [2, 3, 4 , 3, 2, , 4, 52], [1, 2, 3, 4, 5], []]
    expected = [2, 2, False, False]

    result = {}

    test_passed = 0
    for i in range(len(parameters)):
        ret = Solution().findDuplicate(parameters[i])
        if ret != expected[i]:
            return {'errorType': 'WrongAnswer', 'errorMessage': 'Error value: ' + str(parameters[i])}
        test_passed += 1

    result = {'status': 200, 'msg': 'Test passed: ' + str(test_passed)}

    return result
