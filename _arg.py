import argparse

parser = argparse.ArgumentParser(description="사용법 테으슽")

parser.add_argument("--target", required=True, help='어느 것을?')
parser.add_argument("--env", required=False, default='dev', help="환경")

args = parser.parse_args()

print(args.target)
print(args.env)