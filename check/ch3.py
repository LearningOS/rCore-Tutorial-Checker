import base

EXPECTED_3 = [
    # ch3_sleep
    r"get_time OK! (\d+)",
    "Test sleep OK!",

    # ch3_sleep1
    r"current time_msec = (\d+)",
    r"time_msec = (\d+) after sleeping (\d+) ticks, delta = (\d+)ms!",
    "Test sleep1 passed!",

    # ch3_trace
    "string from task trace test",
    "Test trace OK!",
]

if __name__ == "__main__":
    base.test(EXPECTED_3)
