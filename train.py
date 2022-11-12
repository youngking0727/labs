import echonet
import argparse
from echonet.utils.video import run
import ssl

ssl._create_default_https_context = ssl._create_unverified_context



if __name__ == "__main__":
    # Args parser
    parser = argparse.ArgumentParser()
    parser.add_argument("--modelname", type=str, default="r2plus1d_18", help="model name")
    parser.add_argument("--tasks", type=str, default="logBNP", help=" ")
    parser.add_argument("--frames", type=int, default=32, help=" ")
    parser.add_argument("--period", type=int, default=2, help=" ")
    parser.add_argument("--pretrained", type=bool, default=True, help=" ")
    parser.add_argument("--batch_size", type=int, default=8, help=" ")
    args = parser.parse_args()
    run(
        modelname=args.modelname,
        tasks=args.tasks,
        frames=args.frames,
        period=args.period,
        pretrained=args.pretrained,
        batch_size=args.batch_size
    )
