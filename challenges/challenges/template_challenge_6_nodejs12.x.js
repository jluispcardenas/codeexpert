
[USER_FUNCTION]


exports.lambda_handler = async (event) => {
    parameters = [[1,3,4,2,2], [2, 3, 4 , 3, 2, , 4, 52], [1, 2, 3, 4, 5], []]
    expected = [2, 2, false, false]

    var result = {}

    var test_passed = 0
    for (var i = 0; i < parameters.length; i++) {
        var ret = findDuplicate(parameters[i]);
        if (ret != expected[i]) {
            return {'errorType': 'WrongAnswer', 'errorMessage': 'Error value: ' + parameters[i]}
        }
        test_passed += 1
    }

    result = {'status': 200, 'msg': 'Test passed: ' + test_passed}

    return result;
};
