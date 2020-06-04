
[USER_FUNCTION]


exports.lambda_handler = async (event) => {
    parameters = [19, 1, 102, 7, 104]
    expected = [true, true, false, true, false]

    var result = {}

    var test_passed = 0
    for (var i = 0; i < parameters.length; i++) {
        var ret = isHappy(parameters[i]);
        if (ret != expected[i]) {
            return {'errorType': 'WrongAnswer', 'errorMessage': 'Error value: ' + parameters[i]}
        }
        test_passed += 1
    }

    result = {'status': 200, 'msg': 'Test passed: ' + test_passed}

    return result;
};
