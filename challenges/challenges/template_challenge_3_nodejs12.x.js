
[USER_FUNCTION]


exports.lambda_handler = async (event) => {
    parameters = ["1.1.1.1","255.100.50.0","100.0.50.0","1.0.50.100", "1.2.3.4"]
    expected = ["1[.]1[.]1[.]1","255[.]100[.]50[.]0","100[.]0[.]50[.]0","1[.]0[.]50[.]100","1[.]2[.]3[.]4"]

    var result = {}

    var test_passed = 0
    for (var i = 0; i < parameters.length; i++) {
        var ret = defangIPaddr(parameters[i]);
        if (ret != expected[i]) {
            return {'errorType': 'WrongAnswer', 'errorMessage': 'Error value: ' + parameters[i]}
        }
        test_passed += 1
    }

    result = {'status': 200, 'msg': 'Test passed: ' + test_passed}

    return result;
};
