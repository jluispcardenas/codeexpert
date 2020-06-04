
[USER_FUNCTION]


exports.lambda_handler = async (event) => {
    parameters = [5, 4, 3, 2, 0]
    expected = [[[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]], [[1],[1,1],[1,2,1],[1,3,3,1]], [[1],[1,1],[1,2,1]], [[1],[1,1]], []]

    var result = {}

    var test_passed = 0
    for (var i = 0; i < parameters.length; i++) {
        var ret = spiralOrder(parameters[i]);
        if (JSON.stringify(ret) != JSON.stringify(expected[i])) {
            return {'errorType': 'WrongAnswer', 'errorMessage': 'Error value: ' + parameters[i]}
        }
        test_passed += 1
    }

    result = {'status': 200, 'msg': 'Test passed: ' + test_passed}

    return result;
};
