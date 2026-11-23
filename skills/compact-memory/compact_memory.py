import re


def compact_memory(input_text):
    """Convert prose notes to compact symbolic notation.

    Each fact is represented as <TYPE>:<VALUE>
    - note:<content> – a plain note
    - rule:<subject> => <object> – a rule or implication
    - obs:<observation> – an observation
    - task:<description> – a task

    Only one fact per line. No trailing spaces.
    Values may contain any characters except newline.
    """
    if not input_text or not input_text.strip():
        return ''

    raw_lines = input_text.strip().split('\n')
    results = []

    for line in raw_lines:
        line = line.strip()
        if not line:
            continue

        # Split on ". " (period followed by space) as sentence boundary
        if '. ' in line:
            parts = line.split('. ', 1)
            sentence1 = parts[0]  # without the trailing period
            sentence2 = parts[1]  # after period space
        else:
            sentence1 = line
            sentence2 = ''

        # Process sentence1 (strip trailing period for classification, keep cleaned text)
        s1 = sentence1.rstrip('.').strip()
        if s1:
            lower = s1.lower()
            if '=>' in lower:
                parts = lower.split('=>', 1)
                subject = parts[0].strip()
                obj = parts[1].strip()
                if 'should' in lower or 'must' in lower or 'need to' in lower:
                    type_tag = 'task'
                elif 'if' in lower or 'when' in lower:
                    type_tag = 'rule'
                else:
                    type_tag = 'rule'
                results.append(f'{type_tag}:{subject} => {obj}')
            elif any(kw in lower for kw in ['finish', 'implement', 'create', 'build',
                                               'write', 'code', 'develop', 'need to']):
                results.append(f'task:{s1}')
            elif any(kw in lower for kw in ['crucial', 'requirement', 'note', 'remember']):
                results.append(f'note:{s1}')
            else:
                if 'need' in lower or 'want' in lower:
                    results.append(f'task:{s1}')
                else:
                    results.append(f'note:{s1}')

        # Process sentence2 (preserve trailing period if present)
        if sentence2:
            has_trailing_period = sentence2.endswith('.')
            s2_clean = sentence2.rstrip('.').strip()
            lower = s2_clean.lower()

            if '=>' in lower:
                parts = lower.split('=>', 1)
                subject = parts[0].strip()
                obj = parts[1].strip()
                if 'should' in lower or 'must' in lower or 'need to' in lower:
                    type_tag = 'task'
                elif 'if' in lower or 'when' in lower:
                    type_tag = 'rule'
                else:
                    type_tag = 'rule'
                results.append(f'{type_tag}:{subject} => {obj}')
            elif any(kw in lower for kw in ['finish', 'implement', 'create', 'build',
                                               'write', 'code', 'develop', 'need to']):
                results.append(f'task:{sentence2}' if has_trailing_period else f'task:{s2_clean}')
            elif any(kw in lower for kw in ['crucial', 'requirement', 'note', 'remember']):
                results.append(f'note:{sentence2}' if has_trailing_period else f'note:{s2_clean}')
            else:
                if 'need' in lower or 'want' in lower:
                    results.append(f'task:{sentence2}' if has_trailing_period else f'task:{s2_clean}')
                else:
                    results.append(f'note:{sentence2}' if has_trailing_period else f'note:{s2_clean}')

    return '\n'.join(results)
