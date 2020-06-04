
[USER_FUNCTION]


exports.lambda_handler = async (event) => {
    var parameters = [38, 102, 1052, 1, 10234]
    var expected = [2, 3, 8, 1, 1]

    var result = {}

    var test_passed = 0
    for (var i = 0; i < parameters.length; i++) {
        var ret = addDigits(parameters[i]);
        if (ret != expected[i]) {
            return {'errorType': 'WrongAnswer', 'errorMessage': 'Error value: ' + parameters[i]}
        }
        test_passed += 1
    }

    result = {'status': 200, 'msg': 'Test passed: ' + test_passed}

    return result;
};
