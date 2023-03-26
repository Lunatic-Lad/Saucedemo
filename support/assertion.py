from support.assertion_errors import AssertionErrors
class Assertions:
    @staticmethod
    def assertion(actual, expected):
        # self.log.info(f" comparing the expected result: {expected} with the actual result: {actual}")
        assert actual == expected, AssertionErrors.ERROR_MSG_EQUAL.format(expected, actual)
