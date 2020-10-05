from preprocessing import pipeline, profiling

def main():
    df = pipeline('images')
    print(df)

if __name__ == '__main__':
    main()
