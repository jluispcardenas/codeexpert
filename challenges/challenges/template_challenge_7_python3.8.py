import json

[USER_FUNCTION]

def lambda_handler(event, context):
    
    parameters = [5, 4, 3, 2, 0]
    expected = [[[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]], [[1],[1,1],[1,2,1],[1,3,3,1]], [[1],[1,1],[1,2,1]], [[1],[1,1]], []]

    result = {}

    test_passed = 0
    for i in range(len(parameters)):
        ret = Solution().generate(parameters[i])
        if ret != expected[i]:
            return {'errorType': 'WrongAnswer', 'errorMessage': 'Error value: ' + str(parameters[i])}
        test_passed += 1

    result = {'status': 200, 'msg': 'Test passed: ' + str(test_passed)}

    return result
