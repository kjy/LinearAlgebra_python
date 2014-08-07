# version code 988
########                                     ######## 
# Hi there, curious student.                        #
#                                                   #
# This submission script runs some tests on your    #
# code and then uploads it to Coursera for grading. #
#                                                   #
# Changing anything in this script might cause your #
# submissions to fail.                              #
########                                     ########

import io, os, sys, doctest, traceback, importlib, urllib.request, urllib.parse, urllib.error, base64, hashlib, random, ast

SUBMIT_VERSION      = "988"
URL                 = 'matrix-001'
part_friendly_names = ['Int 2 GF2', 'Make Vec', 'Find Candidates', 'Find a and b', 'Divisor of 2461799993978700679']
groups              = [[('GiEBz32fRhO5iB2UE3SzSAIGgO1d1hW7', 'Int 2 GF2', '>>> from GF2 import one\n>>> print(test_format(int2GF2(1)))\n>>> print(test_format(int2GF2(12345)))\n>>> print(test_format(int2GF2(634)))\n>>> print(test_format(int2GF2(3441)))\n>>> print(test_format(int2GF2(0)))\n>>> print(test_format(int2GF2(45321)))\n')], [('GiEBz32fRhO5iB2UP17INIgvqBu0uBVy', 'Make Vec', '>>> from factoring_support import dumb_factor\n>>> l = {257, 2, 3, 277, 5, 7, 137, 11, 13, 271, 17, 19, 269, 149, 23, 281, 283, 29, 31, 163, 37, 167, 41, 43, 173, 47, 229, 179, 53, 59, 151, 61, 181, 193, 67, 197, 71, 73, 241, 79, 83, 139, 89, 199, 223, 263, 97, 227, 131, 101, 103, 233, 107, 109, 239, 157, 113, 211, 251, 293, 191, 127}\n>>> df = dumb_factor(7641, l)\n>>> print(test_format(make_Vec(l, df)))\n>>> print(test_format(l))\n>>> print(test_format(df))\n>>> print(test_format(make_Vec({2, 3, 5, 7}, [(2, 3), (3, 2)])))\n>>> print(test_format(make_Vec({2, 3, 5, 7, 137, 11, 13, 17, 19, 149, 23, 29, 31, 163, 37, 167, 41, 43, 173, 47, 179, 53, 59, 151, 61, 181, 193, 67, 197, 71, 73, 79, 83, 139, 89, 199, 97, 131, 101, 103, 107, 109, 157, 113, 191, 127}, dumb_factor(5432, {2, 3, 5, 7, 137, 11, 13, 17, 19, 149, 23, 29, 31, 163, 37, 167, 41, 43, 173, 47, 179, 53, 59, 151, 61, 181, 193, 67, 197, 71, 73, 79, 83, 139, 89, 199, 97, 131, 101, 103, 107, 109, 157, 113, 191, 127}))))\n')], [('GiEBz32fRhO5iB2UiyOmwC3BuYmiZfL0', 'Find Candidates', '>>> print(test_format(type(find_candidates(100, primes(7))) == tuple))\n>>> p = primes(32)\n>>> rowlist, roots = find_candidates(2419, p)\n>>> print(test_format((rowlist[:1+len(p)], roots[:1+len(p)])))\n>>> p = primes(30)\n>>> rowlist, roots = find_candidates(1234, p)\n>>> print(test_format((rowlist[:1+len(p)], roots[:1+len(p)])))\n>>> p = primes(50)\n>>> rowlist, roots = find_candidates(65231, p)\n>>> print(test_format((rowlist[:1+len(p)], roots[:1+len(p)])))\n')], [('GiEBz32fRhO5iB2UdVp7MX3aT4O0ULkn', 'Find a and b', '>>> v = Vec({0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11},{0: 0, 1: one, 2: one, 4: 0, 5: one, 11: one})\n>>> N = 2419\n>>> roots = [51, 52, 53, 58, 61, 62, 63, 67, 68, 71, 77, 79]\n>>> print(test_format(find_a_and_b(v, roots, N)))\n>>> v = Vec({0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11},{0: 0, 1: 0, 10: one, 2: one})\n>>> N = 2419\n>>> roots = [51, 52, 53, 58, 61, 62, 63, 67, 68, 71, 77, 79]\n>>> print(test_format(find_a_and_b(v, roots, N)))\n')], [('GiEBz32fRhO5iB2UJvOtHoslL9WjB0uY', 'Divisor of 2461799993978700679', '>>> print(test_format(smallest_nontrivial_divisor_of_2461799993978700679))\n')]]
source_files        = ['factoring_lab.py'] * len(sum(groups,[]))

try:
    import factoring_lab as solution
    test_vars = vars(solution).copy()
except Exception as exc:
    print(exc)
    print("!! It seems like you have an error in your stencil file. Please fix before submitting.")
    sys.exit(1)

def find_lines(varname):
    return list(filter(lambda l: varname in l, list(open("python_lab.py"))))

def find_line(varname):
    ls = find_lines(varname)
    return ls[0] if len(ls) else None


def use_comprehension(varname):
    lines = find_lines(varname)
    for line in lines:
        try:
            if "comprehension" in ast.dump(ast.parse(line)):
                return True
        except: pass
    return False

def double_comprehension(varname):
    line = find_line(varname)
    return ast.dump(ast.parse(line)).count("comprehension") == 2

def line_contains_substr(varname, word):
    lines = find_line(varname)
    for line in lines:
        if word in line:
            return True
    return False

def test_format(obj, precision=6):
    tf = lambda o: test_format(o, precision)
    delimit = lambda o: ', '.join(o)
    otype = type(obj)
    if otype is str:
        return "'%s'" % obj
    elif otype is float or otype is int:
        if otype is int:
            obj = float(obj)
        if -0.000001 < obj < 0.000001:
            obj = 0.0
        fstr = '%%.%df' % precision
        return fstr % obj
    elif otype is set:
        if len(obj) == 0:
            return 'set()'
        return '{%s}' % delimit(sorted(map(tf, obj)))
    elif otype is dict:
        return '{%s}' % delimit(sorted(tf(k)+': '+tf(v) for k,v in obj.items()))
    elif otype is list:
        return '[%s]' % delimit(map(tf, obj))
    elif otype is tuple:
        return '(%s%s)' % (delimit(map(tf, obj)), ',' if len(obj) is 1 else '')
    elif otype.__name__ in ['Vec','Mat']:
        entries = tf({x:obj.f[x] for x in obj.f if tf(obj.f[x]) != tf(0)})
        return '%s(%s, %s)' % (otype.__name__, test_format(obj.D), entries)
    else:
        return str(obj)



def output(tests):
    dtst = doctest.DocTestParser().get_doctest(tests, test_vars, 0, '<string>', 0)
    runner = ModifiedDocTestRunner()
    runner.run(dtst)
    return runner.results

test_vars['test_format'] = test_vars['tf'] = test_format
test_vars['find_lines'] = find_lines
test_vars['find_line'] = find_line
test_vars['use_comprehension'] = use_comprehension
test_vars['double_comprehension'] = double_comprehension
test_vars['line_contains_substr'] = line_contains_substr

base_url = '://class.coursera.org/%s/assignment/' % URL
protocol = 'https'
colorize = False
verbose  = False

class ModifiedDocTestRunner(doctest.DocTestRunner):
    def __init__(self, *args, **kwargs):
        self.results = []
        return super(ModifiedDocTestRunner, self).__init__(*args, checker=OutputAccepter(), **kwargs)
    
    def report_success(self, out, test, example, got):
        self.results.append(got)
    
    def report_unexpected_exception(self, out, test, example, exc_info):
        exf = traceback.format_exception_only(exc_info[0], exc_info[1])[-1]
        self.results.append(exf)

class OutputAccepter(doctest.OutputChecker):
    def check_output(self, want, got, optionflags):
        return True

def submit(parts_string, login, password):   
    print('= Coding the Matrix Homework and Lab Submission')
    
    if not login:
        login = login_prompt()
    if not password:
        password = password_prompt()
    if not parts_string: 
        parts_string = parts_prompt()

    parts = parse_parts(parts_string)

    if not all([parts, login, password]):
        return

    for sid, name, part_tests in parts:
        sys.stdout.write('== Submitting "%s"' % name)

        if 'DEV' in os.environ: sid += '-dev'

        (login, ch, state, ch_aux) = get_challenge(login, sid)

        if not all([login, ch, state]):
            print('  !! Error: %s\n' % login)
            return

        # to stop Coursera's strip() from doing anything, we surround in parens
        results  = output(part_tests)
        prog_out = '(%s)' % ''.join(map(str.rstrip, results))
        token    = challenge_response(login, password, ch)
        src      = source(sid)

        feedback = submit_solution(login, token, sid, prog_out, src, state, ch_aux)

        if len(feedback.strip()) > 0:
            if colorize:
                good = 'incorrect' not in feedback.lower()
                print(': \033[1;3%dm%s\033[0m' % (2 if good else 1, feedback.strip()))
            else:
                print(': %s' % feedback.strip())
        
        if verbose:
            res_itr = iter(results)
            for t in part_tests.split('\n'):
                print(t)
                if t[:3] == '>>>':
                   sys.stdout.write(next(res_itr)) 
            # print(part_tests)
            # print(results)
            # for t, r in zip(part_tests.split('\n>>>'), results):
            #     sys.stdout.write('>>> %s\n%s' % (t, r))
            sys.stdout.write('\n\n')


def login_prompt():
    return input('Login email address: ')


def password_prompt():
    return input("One-time password from the assignment page (NOT your own account's password): ")


def parts_prompt():
    print('These are the assignment parts that you can submit:')

    for i, name in enumerate(part_friendly_names):
        print('  %d) %s' % (i+1, name))

    return input('\nWhich parts do you want to submit? (Ex: 1, 4-7): ')

def parse_parts(string):
    def extract_range(s):
        s = s.split('-')
        if len(s) == 1: return [int(s[0])]
        else: return list(range(int(s[0]), 1+int(s[1])))
    parts = map(extract_range, string.split(','))
    flat_parts = sum(parts, [])
    return sum(list(map(lambda p: groups[p-1], flat_parts)),[])

def get_challenge(email, sid):
    """Gets the challenge salt from the server. Returns (email,ch,state,ch_aux)."""
    params = {'email_address': email, 'assignment_part_sid': sid, 'response_encoding': 'delim'}

    challenge_url = '%s%schallenge' % (protocol, base_url)
    data = urllib.parse.urlencode(params).encode('utf-8')
    req  = urllib.request.Request(challenge_url, data)
    resp = urllib.request.urlopen(req)
    text = resp.readall().decode('utf-8').strip().split('|')

    if len(text) != 9:
        print('  !! %s' % '|'.join(text))
        sys.exit(1)
  
    return tuple(text[x] for x in [2,4,6,8])


def challenge_response(email, passwd, challenge):
    return hashlib.sha1((challenge+passwd).encode('utf-8')).hexdigest()


def submit_solution(email_address, ch_resp, sid, output, source, state, ch_aux):
    b64ize = lambda s: str(base64.encodebytes(s.encode('utf-8')), 'ascii')

    values = { 'assignment_part_sid' : sid
             , 'email_address'       : email_address
             , 'submission'          : b64ize(output) 
             , 'submission_aux'      : b64ize(source)
             , 'challenge_response'  : ch_resp
             , 'state'               : state
             }

    submit_url = '%s%ssubmit' % (protocol, base_url)
    data     = urllib.parse.urlencode(values).encode('utf-8')
    req      = urllib.request.Request(submit_url, data)
    response = urllib.request.urlopen(req)

    return response.readall().decode('utf-8').strip()


def source(sid):
    src = ['# submit version: %s' % SUBMIT_VERSION]
    for fn in set(source_files):
        with open(fn) as source_f:
            src.append(source_f.read())
    return '\n\n'.join(src)


if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser()
    env = os.environ
    helps = [ 'numbers or ranges of tasks to submit'
            , 'the email address on your Coursera account'
            , 'your ONE-TIME password'
            , 'use ANSI color escape sequences'
            , 'show the test\'s interaction with your code'
            , 'use an encrypted connection to Coursera'
            , 'use an unencrypted connection to Coursera'
            ]
    parser.add_argument('tasks',      default=env.get('COURSERA_TASKS'), nargs='*', help=helps[0])
    parser.add_argument('--email',    default=env.get('COURSERA_EMAIL'),            help=helps[1])
    parser.add_argument('--password', default=env.get('COURSERA_PASS'),             help=helps[2])
    parser.add_argument('--colorize', default=False, action='store_true',           help=helps[3])
    parser.add_argument('--verbose',  default=False, action='store_true',           help=helps[4])
    group = parser.add_mutually_exclusive_group()
    group.add_argument('--https', dest="protocol", const="https", action="store_const", help=helps[-2])
    group.add_argument('--http',  dest="protocol", const="http",  action="store_const", help=helps[-1])
    args = parser.parse_args()
    if args.protocol: protocol = args.protocol
    colorize = args.colorize
    verbose = args.verbose
    submit(','.join(args.tasks), args.email, args.password)

