import sentry_sdk

sdn = "http://7596466671c94dbfaa436bbb3fea63b1@192.168.154.130:9000/2"

sentry_sdk.init("http://7596466671c94dbfaa436bbb3fea63b1@192.168.154.130:9000/2")

division_by_zero = 1 / 0