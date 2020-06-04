import json

[USER_FUNCTION]

def lambda_handler(event, context):
    
    parameters = [[[ 1, 2, 3 ],[ 4, 5, 6 ],[ 7, 8, 9 ]], [[1,2,3,4,5],[6,7,8,9,10],[11,12,13,14,15],[16,17,18,19,20],[21,22,23,24,25]], [[1,2],[3,4]]]
    expected = [[1,2,3,6,9,8,7,4,5], [1,2,3,4,5,10,15,20,25,24,23,22,21,16,11,6,7,8,9,14,19,18,17,12,13], [1,2,4,3]]

    result = {}

    test_passed = 0
    for i in range(len(parameters)):
        ret = Solution().spiralMatrix(parameters[i])
        if ret != expected[i]:
            return {'errorType': 'WrongAnswer', 'errorMessage': 'Error value: ' + str(parameters[i])}
        test_passed += 1

    result = {'status': 200, 'msg': 'Test passed: ' + str(test_passed)}

    return result
