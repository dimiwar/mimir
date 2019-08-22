# define risk level ranges
# mapped to Estimative language
# used to describe quality and credibility of underlying sources, data, and methodologies based Intelligence Community Directive 203 (ICD 203) and JP 2-0, Joint Intelligence

risk_ranges = {
    "almost-no-chance": (0, 4),
    'very-unlikely': (5, 19),
    'unlikely': (20, 44),
    'roughly-even-chance': (45, 54),
    'likely': (55, 79),
    'very-likely': (80, 94),
    'almost-certain': (95, 100)
}
