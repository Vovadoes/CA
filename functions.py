from math import pi
from Monitor import getMonitors
from settings import STANDART_DPI



def get_super(x):
    normal = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+-=()"
    super_s = "ᴬᴮᶜᴰᴱᶠᴳᴴᴵᴶᴷᴸᴹᴺᴼᴾQᴿˢᵀᵁⱽᵂˣʸᶻᵃᵇᶜᵈᵉᶠᵍʰᶦʲᵏˡᵐⁿᵒᵖ۹ʳˢᵗᵘᵛʷˣʸᶻ⁰¹²³⁴⁵⁶⁷⁸⁹⁺⁻⁼⁽⁾"
    res = x.maketrans(''.join(normal), ''.join(super_s))
    return x.translate(res)


def get_sub(x):
    normal = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+-=()"
    sub_s = "ₐ₈CDₑբGₕᵢⱼₖₗₘₙₒₚQᵣₛₜᵤᵥwₓᵧZₐ♭꜀ᑯₑբ₉ₕᵢⱼₖₗₘₙₒₚ૧ᵣₛₜᵤᵥwₓᵧ₂₀₁₂₃₄₅₆₇₈₉₊₋₌₍₎"
    res = x.maketrans(''.join(normal), ''.join(sub_s))
    return x.translate(res)


def degrees_to_radians(angle: float) -> float:
    return angle * pi / 180


def change_size(window):
    screen = window.screen()
    monitors = getMonitors()
    monitor = monitors[screen.name()]
    print(screen.name(), monitor.get_max_dpi())
    k = monitor.get_max_dpi() / STANDART_DPI
    size = round(window.size().width() * k), round(window.size().height() * k)
    # size = window.sizeHint().width(), window.sizeHint().height()
    if k > 1:
        window.setMinimumSize(*size)
        window.setMaximumSize(*size)
        # window.setMinimumSize(0, 0)
        # window.setMaximumSize(10000, 10000)
        window.setBaseSize(*size)


def radians_to_degrees(angle_rad: float) -> float:
    return angle_rad * 180 / pi
