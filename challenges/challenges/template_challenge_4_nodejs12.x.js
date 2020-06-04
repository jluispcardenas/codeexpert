
[USER_FUNCTION]


exports.lambda_handler = async (event) => {
    parameters = ["A", "AB", "ABB", "ZY", "XYZ"]
    expected = [1, 28, 730, 701, 16900]

    var result = {}

    var test_passed = 0
    for (var i = 0; i < parameters.length; i++) {
        var ret = titleToNumber(parameters[i]);
        if (ret != expected[i]) {
            return {'errorType': 'WrongAnswer', 'errorMessage': 'Error value: ' + parameters[i]}
        }
        test_passed += 1
    }

    result = {'status': 200, 'msg': 'Test passed: ' + test_passed}

    return result;
};
