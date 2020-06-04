
[USER_FUNCTION]


exports.lambda_handler = async (event) => {
    parameters = ["()", "()[]{}", "(]", "([)]", "{[]}"]
    expected = [true, true, false, false, true]

    var result = {}

    var test_passed = 0
    for (var i = 0; i < parameters.length; i++) {
        var ret = isValid(parameters[i]);
        if (ret != expected[i]) {
            return {'errorType': 'WrongAnswer', 'errorMessage': 'Error value: ' + parameters[i]}
        }
        test_passed += 1
    }

    result = {'status': 200, 'msg': 'Test passed: ' + test_passed}

    return result;
};
