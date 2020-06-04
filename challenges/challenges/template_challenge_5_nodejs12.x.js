
[USER_FUNCTION]


exports.lambda_handler = async (event) => {
    parameters = [[3,2,3],[2,2,1,1,1,2,2],[4,3,4,2,2,3,4,4,5,6,7,4,4,4,4,4]]
    expected = [3,2,4]

    var result = {}

    var test_passed = 0
    for (var i = 0; i < parameters.length; i++) {
        var ret = majorityElement(parameters[i]);
        if (ret != expected[i]) {
            return {'errorType': 'WrongAnswer', 'errorMessage': 'Error value: ' + parameters[i]}
        }
        test_passed += 1
    }

    result = {'status': 200, 'msg': 'Test passed: ' + test_passed}

    return result;
};
