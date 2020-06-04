import json

[USER_FUNCTION]

def lambda_handler(event, context):
    
    parameters = ["1.1.1.1","255.100.50.0","100.0.50.0","1.0.50.100", "1.2.3.4"]
    expected = ["1[.]1[.]1[.]1","255[.]100[.]50[.]0","100[.]0[.]50[.]0","1[.]0[.]50[.]100","1[.]2[.]3[.]4"]

    result = {}

    test_passed = 0
    for i in range(len(parameters)):
        ret = Solution().defangIPaddr(parameters[i])
        if ret != expected[i]:
            return {'errorType': 'WrongAnswer', 'errorMessage': 'Error value: ' + str(parameters[i])}
        test_passed += 1

    result = {'status': 200, 'msg': 'Test passed: ' + str(test_passed)}

    return result
