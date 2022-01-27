from app import main, print_pretty


def test_myoutput(capsys):
    """Testing the realisation with example from https://github.com/mnv/python-basics"""
    test_data = ((1, 4), (4, 1), (5, 5), (7, 2))
    test_string = "(0, 1) -> (1, 4)[3.1622776601683795] " \
                  "-> (4, 1)[7.404918347287664] " \
                  "-> (5, 5)[11.528023972905324] " \
                  "-> (7, 2)[15.133575248369313] " \
                  "-> (0, 1)[22.204643060234787] = 22.204643060234787"
    result = main(test_data)
    for i in result:
        print_pretty(i)
    captured = capsys.readouterr()
    assert test_string in captured.out
