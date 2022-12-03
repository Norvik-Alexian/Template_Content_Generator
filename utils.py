import config


def prettify(content: str, finish_reason: str):
    if finish_reason == 'length':
        ending_punctuations = config.ENDING_PUNCTUATIONS
        any_finished_sequence = any([mark in content for mark in ending_punctuations])
        if any_finished_sequence:
            reversed_content = content[::-1]
            last_finished_sequence = len(content) - 1 - min(
                [reversed_content.index(mark) for mark in ending_punctuations if mark in content]
            )
            content = content[:last_finished_sequence + 1]

    content = config.SPACE_REMOVER_PATTERN.sub(' ', content)

    return content