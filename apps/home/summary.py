def summarize(input_text,value):
    from textsum.summarize import Summarizer

    model_name = "pszemraj/led-large-book-summary"
    summarizer = Summarizer(
        model_name_or_path=model_name,  # you can use any Seq2Seq model on the Hub
        token_batch_length=4096,  # tokens to batch summarize at a time, up to 16384
        max_length=value,
        min_length=150
    )
    long_string = input_text
    out_str = summarizer.summarize_string(long_string)
    return out_str