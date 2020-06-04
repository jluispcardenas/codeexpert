import json

[USER_FUNCTION]

def lambda_handler(event, context):
    
    parameters = [[3,2,3],[2,2,1,1,1,2,2],[4,3,4,2,2,3,4,4,5,6,7,4,4,4,4,4]]
    expected = [3,2,4]

    result = {}

    test_passed = 0
    for i in range(len(parameters)):
        ret = Solution().majorityElement(parameters[i])
        if ret != expected[i]:
            return {'errorType': 'WrongAnswer', 'errorMessage': 'Error value: ' + str(parameters[i])}
        test_passed += 1

    result = {'status': 200, 'msg': 'Test passed: ' + str(test_passed)}

    return result
