import argparse
parser = argparse.ArgumentParser()
parser.add_argument("luku1", help="syota luku 1", type=int)
parser.add_argument("luku2", help="syota luku 1", type=int)
args = parser.parse_args()
print(args.luku1 + args.luku2)
print(max(args.luku1 + args.luku2))
print(min(args.luku1 + args.luku2))

#tehtävässä luvut syötetään komentoriville