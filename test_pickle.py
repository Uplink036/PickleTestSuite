import pickle
import pytest
import random
from hashlib import sha256
from pickle import dumps, PicklingError
from hypothesis import settings, given, seed, strategies as st
from hypothesis.strategies import composite
from logger import save_unpickled_test,clean_folder
from classes_functions import *
from decimal import *

random.setstate((3, (2147483648, 2482047965, 3950236897, 2833011536, 3655160018, 2107462491, 1405585727, 1059851751, 1428215185, 965241707, 53506477, 2275269889, 580485935, 2418778002, 2083784972, 328010327, 1017714149, 1595693566, 2152402094, 3341165751, 1559722753, 1463506044, 1529096010, 2002838235, 3270377632, 2986422339, 1522193462, 3651469921, 1321873126, 1073595227, 3209625307, 1416752828, 4281756648, 3316967646, 88546615, 2955950634, 3063668351, 1226222720, 4286466871, 2155236041, 3978118053, 1998571129, 3495543307, 1616175122, 3084568286, 2625189560, 33766510, 1074041223, 1550599718, 1784902695, 44895503, 863379457, 3519379007, 3701737594, 3295637009, 449738323, 1496910703, 1439513020, 1114667596, 2649402284, 2219700182, 3695751793, 3033872917, 1309914409, 2819676169, 3722054968, 2571382399, 2920683432, 1526529927, 3808833080, 1175574391, 46187916, 907770954, 1467457550, 1292206058, 3394314966, 1801887486, 3492846718, 2322277442, 2329002867, 1428035188, 667665074, 392923259, 2752927018, 2133642932, 2808698566, 1957231968, 1288382947, 2441479690, 25290287, 955575320, 1860511698, 1183567975, 698250086, 1444989879, 1581516381, 626287196, 3727774069, 2818053307, 128452108, 4234527433, 1070496644, 2467776741, 152426728, 631906688, 2634876177, 2270169546, 3766554726, 4199129290, 1217750469, 1434043381, 374884339, 1209604032, 4268346223, 3860663234, 1695259458, 3972921426, 763612251, 837652533, 2844779954, 1425648453, 4039174335, 27711332, 2601168520, 3471152469, 1826441821, 2941985768, 685385632, 2723110314, 968616483, 3487026754, 1101682220, 2459473172, 804569002, 2869340717, 1035078183, 820096057, 548618674, 1778013428, 4196424540, 2040253794, 1386505935, 3033697944, 1917090784, 3146192815, 1876290520, 666291213, 164772718, 417493505, 209431892, 882087166, 3273148033, 1077197999, 1256536837, 2126406282, 953538111, 105286940, 2416398052, 3233317770, 2738975985, 2901880377, 2131258753, 1303501849, 2130792227, 1090725180, 2071593060, 3304298166, 3585189721, 2843516573, 3955007360, 1759756353, 2374604399, 3553383205, 1735295587, 1608704643, 2267742318, 1626939102, 437410884, 1314446534, 440726064, 1922625031, 2689289885, 2173372357, 772987479, 3782258376, 3252515574, 1272703980, 3864782021, 1866271703, 119639719, 1860440293, 1344398172, 2258151583, 1419796258, 1806377307, 344615271, 2752597897, 2225109578, 3081900469, 2822142669, 3466916359, 1200572190, 3349416940, 499601203, 2590050652, 2708011453, 903141717, 2253074865, 1500685110, 1299701929, 4247337959, 3783884608, 241222636, 2862919284, 3738779246, 3394312925, 3421855741, 498476300, 59294278, 3558486204, 1070244890, 3003899935, 17914187, 933478913, 3967095021, 1858771562, 1703706436, 2175622028, 1036899787, 1046719969, 3502952453, 2476367219, 2394339714, 2413065824, 1232055644, 1542247600, 1416899940, 1838067092, 3758453600, 3367823345, 3725121525, 2026658953, 3216452258, 1738345796, 3536756788, 2093132126, 426568683, 962351722, 4083161983, 295839192, 667539144, 2513798727, 931354157, 3900292866, 3593053580, 940504886, 48836817, 2297046170, 1841514252, 2543695696, 1895183051, 2379172580, 946317690, 736194053, 3444980547, 1150282907, 440340707, 2746555190, 3199936399, 2992378382, 1036421647, 2522585910, 3885165966, 1038723251, 2598681211, 3794625949, 696764522, 1624151800, 3987229383, 4293767229, 3762022871, 188777698, 3233027336, 4115724736, 993387976, 4111843970, 3384669911, 3927163653, 534359258, 2562919780, 4044007584, 3852586357, 2212154349, 4159852476, 2731582253, 3406966404, 752848617, 2449351762, 1031773073, 1640451820, 2146882312, 944279935, 2517952897, 4197459876, 3380718011, 1568676378, 513974283, 622771475, 1454961453, 827146772, 2834913254, 3307901840, 3371557921, 4254499811, 3735436700, 2475786187, 677614636, 1806588800, 761188361, 460883689, 1720989556, 1063422491, 3119882019, 3390465468, 2333224711, 400877503, 2846196567, 2231973490, 3766377240, 2997764417, 1188688816, 4141235618, 2644077919, 2505462126, 787817322, 3321569521, 2662569153, 2670113637, 3350031269, 2464150942, 1239857410, 1045351058, 1168606720, 1699097138, 2139019637, 2207162773, 1461121883, 2879764628, 1693572190, 3353168734, 70856973, 202360167, 45743737, 4140659927, 1313665471, 96475712, 4172837094, 2605878822, 1251343899, 8715313, 3080086318, 1340801870, 2731571395, 2636666847, 1903770390, 3321701692, 1256161542, 358239828, 2986963268, 2338684342, 3853477167, 3840188962, 3773662950, 643392944, 2070880484, 3923664475, 726582580, 2826018697, 1659831794, 1825602804, 1647212384, 3776511806, 2042687223, 1134083448, 3569608308, 450853838, 1059660876, 1868031623, 3808940848, 2901839315, 2861002320, 1716062355, 186267112, 2623881456, 2931952731, 4268257519, 3771892088, 752901104, 1164347456, 1194006482, 2207830467, 2202194459, 774448876, 2220799005, 1492352884, 2462143136, 1337365021, 894901362, 2361597290, 1787620955, 4158242718, 4182459679, 1537204063, 688336767, 1311825662, 1763561618, 2498211537, 1305775916, 1717857879, 666295102, 3503714314, 984533796, 3670696154, 3348146425, 2868423140, 3741040572, 2560882723, 508643899, 232992698, 1024061887, 3938533817, 691458015, 2594849320, 2799656766, 1123949519, 335856151, 185289007, 299986256, 292797256, 1745368433, 2943835531, 3286006290, 2690946538, 4138161437, 1850292959, 3499222547, 1450217770, 2298985242, 4261517685, 4158396620, 2813515729, 583128124, 2394857089, 965389040, 2262491964, 1943606173, 851079013, 2651904619, 1798364358, 3243356641, 2401725772, 237635963, 4160989000, 847239269, 1012648061, 2749724117, 4113240625, 1070809267, 3670740615, 2259137054, 813613119, 3847510310, 2847029029, 414166093, 1157238178, 2721874016, 1699364727, 3374201609, 3857608030, 1157625537, 3616972677, 3105332780, 1702651992, 2870305658, 1997129220, 1390228886, 4212143705, 2571031775, 2622971859, 3703459161, 2230564328, 3889919013, 3130686982, 3514920071, 4184277845, 3178966873, 4142159324, 1034767741, 1851797731, 3169790392, 2875534580, 2037434240, 38046853, 1619920770, 925588964, 1213281304, 4029208975, 906707481, 2910190096, 2721329948, 2525573464, 3749462236, 3538081983, 1234171740, 3235467690, 3058063530, 1162731203, 2964406419, 4060064751, 2031097886, 932641172, 2258006658, 642097568, 2815345508, 1328868193, 845605658, 4092219476, 2530898247, 382565376, 2177203075, 3150119557, 4194771771, 644090245, 2313620303, 741545600, 1551024324, 1695952156, 545361494, 4078208244, 3563015430, 821788670, 1289135223, 1367258734, 3482335660, 1150894422, 1472877152, 2757744325, 3222143717, 118280038, 2657998761, 2924412477, 1023192060, 266745764, 1502304579, 587372476, 1533782728, 2903473542, 177267389, 2866613968, 3111670542, 3729741567, 3442283893, 2655343308, 2867294694, 3633856940, 3912238352, 3327582331, 2828424286, 3237549161, 160986633, 756271504, 125339818, 466779225, 634560170, 2099959832, 4030419545, 2573955951, 3365021404, 2234048383, 879828688, 1708634702, 1981084388, 2752788746, 3935458738, 717576756, 2661558741, 542198443, 1568657631, 2688886826, 2186865390, 2700751942, 4144753172, 1198303372, 3251614215, 2074817183, 2901200427, 3465635309, 284203335, 3316520024, 2289647995, 641879799, 1142862631, 3401876640, 1766931531, 3341286643, 2513177443, 721405881, 370967534, 2762142673, 2149767442, 3001215621, 3215965447, 116623117, 3060724694, 3540544458, 4084656948, 2344441641, 1686253356, 2209382893, 1337888858, 1749253770, 2098090342, 3436888241, 4253574870, 624), None))
settings.register_profile("first", max_examples=100, deadline=None)
settings.load_profile("first")

logger = True

@composite
def one_dim_random_strategy(draw):
    result = []
    result.append(draw(st.integers()))
    result.append(draw(st.floats(allow_nan=False)))
    result.append(draw(st.text()))
    result.append(draw(st.booleans()))
    result.append(draw(st.binary()))
    result.append(draw(st.just(None)))
    result.append(draw(st.just(Ellipsis)))
    result.append(draw(st.just(NotImplemented)))
    result.append(draw(st.complex_numbers(allow_nan=False)))

    ret = draw(st.sampled_from(result))
    return ret

# @composite
# def two_dim_random_strategy(draw):
#     result = []
#     result.append(draw(st.integers()))
#     result.append(draw(st.floats(allow_nan=False)))
#     result.append(draw(st.text()))
#     result.append(draw(st.booleans()))
#     result.append(draw(st.binary()))
#     result.append(draw(st.just(None)))
#     result.append(draw(st.just(Ellipsis)))
#     result.append(draw(st.just(NotImplemented)))
#     result.append(draw(st.complex_numbers(allow_nan=False)))
#     result.append(draw(st.lists(elements=one_dim_random_strategy())))
#     result.append(draw(st.sets(elements=one_dim_random_strategy())))
#     result.append(draw(st.dictionaries(keys=st.text(), values=one_dim_random_strategy())))
#     result.append(draw(st.tuples(st.integers(), st.floats(allow_nan=False), st.text(), st.booleans())))


#     ret = draw(st.sampled_from(result))
#     return ret

class TestPickle:
    @seed(1)
    @given(st.just(None))
    def test_none(self, data):
        for i in range(0, pickle.HIGHEST_PROTOCOL + 1):
            try:
                dump_a1 = dumps(data, protocol=i)
                dump_a2 = dumps(data, protocol=i)
            except PicklingError as e:
                print(f"Error in pickling: {data} - error: {e}")
                raise ValueError(f"Error in pickling: {data} - error: {e}")

            try:
                h_a1 = sha256(dump_a1).hexdigest()
                h_a2 = sha256(dump_a2).hexdigest()
            except Exception as e:
                print(f"Error in hashing: {data} - error: {e}")
                raise ValueError(f"Error in pickling: {data} - error: {e}")

            assert h_a1 == h_a2
            if logger:
                save_unpickled_test(data=h_a1, comment="None", protocol=i)

    @seed(2)
    @given(st.booleans())
    def test_booleans(self, data):
        for i in range(0, pickle.HIGHEST_PROTOCOL + 1):
            try:
                dump_a1 = dumps(data, protocol=i)
                dump_a2 = dumps(data, protocol=i)
            except PicklingError as e:
                print(f"Error in pickling: {data} - error: {e}")
                raise ValueError(f"Error in pickling: {data} - error: {e}")

            try:
                h_a1 = sha256(dump_a1).hexdigest()
                h_a2 = sha256(dump_a2).hexdigest()
            except Exception as e:
                print(f"Error in hashing: {data} - error: {e}")
                raise ValueError(f"Error in pickling: {data} - error: {e}")

            assert h_a1 == h_a2
            if logger:
                save_unpickled_test(h_a1, comment="Boolean", protocol=i)

    @seed(3)
    @given(st.just(Ellipsis))
    def test_ellipsis(self, data):
        for i in range(0, pickle.HIGHEST_PROTOCOL + 1):
            try:
                dump_a1 = dumps(data, protocol=i)
                dump_a2 = dumps(data, protocol=i)
            except PicklingError as e:
                print(f"Error in pickling: {data} - error: {e}")
                raise ValueError(f"Error in pickling: {data} - error: {e}")

            try:
                h_a1 = sha256(dump_a1).hexdigest()
                h_a2 = sha256(dump_a2).hexdigest()
            except Exception as e:
                print(f"Error in hashing: {data} - error: {e}")
                raise ValueError(f"Error in pickling: {data} - error: {e}")

            assert h_a1 == h_a2
            if logger:
                save_unpickled_test(data=h_a1, comment="Ellipsis", protocol=i)

    @seed(4)
    @given(st.just(NotImplemented))
    def test_notimplemented(self, data):
        for i in range(0, pickle.HIGHEST_PROTOCOL + 1):
            try:
                dump_a1 = dumps(data, protocol=i)
                dump_a2 = dumps(data, protocol=i)
            except PicklingError as e:
                print(f"Error in pickling: {data} - error: {e}")
                raise ValueError(f"Error in pickling: {data} - error: {e}")

            try:
                h_a1 = sha256(dump_a1).hexdigest()
                h_a2 = sha256(dump_a2).hexdigest()
            except Exception as e:
                print(f"Error in hashing: {data} - error: {e}")
                raise ValueError(f"Error in pickling: {data} - error: {e}")

            assert h_a1 == h_a2
            if logger:
                save_unpickled_test(data=h_a1, comment="NotImplemented", protocol=i)

    @seed(5)
    @given(st.integers())
    def test_integers(self, data):
        for i in range(0, pickle.HIGHEST_PROTOCOL + 1):
            try:
                dump_a1 = dumps(data, protocol=i)
                dump_a2 = dumps(data, protocol=i)
            except PicklingError as e:
                print(f"Error in pickling: {data} - error: {e}")
                raise ValueError(f"Error in pickling: {data} - error: {e}")

            try:
                h_a1 = sha256(dump_a1).hexdigest()
                h_a2 = sha256(dump_a2).hexdigest()
            except Exception as e:
                print(f"Error in hashing: {data} - error: {e}")
                raise ValueError(f"Error in pickling: {data} - error: {e}")

            assert h_a1 == h_a2
            if logger:
                save_unpickled_test(data=h_a1, comment="Integer",json_data = str(data), protocol=i)

    @seed(6)
    @given(st.floats(allow_nan=False))
    def test_floats(self, data):
        for i in range(0, pickle.HIGHEST_PROTOCOL + 1):
            try:
                dump_a1 = dumps(data, protocol=i)
                dump_a2 = dumps(data, protocol=i)
            except PicklingError as e:
                print(f"Error in pickling: {data} - error: {e}")
                raise ValueError(f"Error in pickling: {data} - error: {e}")

            try:
                h_a1 = sha256(dump_a1).hexdigest()
                h_a2 = sha256(dump_a2).hexdigest()
            except Exception as e:
                print(f"Error in hashing: {data} - error: {e}")
                raise ValueError(f"Error in pickling: {data} - error: {e}")

            assert h_a1 == h_a2
            if logger:
                save_unpickled_test(h_a1, comment="Float",json_data = str(data), protocol=i)

    @seed(7)
    @given(st.complex_numbers(allow_nan=False))
    def test_complex_numbers(self, data):
        for i in range(0, pickle.HIGHEST_PROTOCOL + 1):
            try:
                dump_a1 = dumps(data, protocol=i)
                dump_a2 = dumps(data, protocol=i)
            except PicklingError as e:
                print(f"Error in pickling: {data} - error: {e}")
                raise ValueError(f"Error in pickling: {data} - error: {e}")

            try:
                h_a1 = sha256(dump_a1).hexdigest()
                h_a2 = sha256(dump_a2).hexdigest()
            except Exception as e:
                print(f"Error in hashing: {data} - error: {e}")
                raise ValueError(f"Error in pickling: {data} - error: {e}")

            assert h_a1 == h_a2
            if logger:
                save_unpickled_test(data=h_a1, comment="Complex", protocol=i)

    @seed(8)
    @given(st.text())
    def test_text(self, data):
        for i in range(0, pickle.HIGHEST_PROTOCOL + 1):
            try:
                dump_a1 = dumps(data, protocol=i)
                dump_a2 = dumps(data, protocol=i)
            except PicklingError as e:
                print(f"Error in pickling: {data} - error: {e}")
                raise ValueError(f"Error in pickling: {data} - error: {e}")

            try:
                h_a1 = sha256(dump_a1).hexdigest()
                h_a2 = sha256(dump_a2).hexdigest()
            except Exception as e:
                print(f"Error in hashing: {data} - error: {e}")
                raise ValueError(f"Error in pickling: {data} - error: {e}")

            assert h_a1 == h_a2
            if logger:
                save_unpickled_test(data=h_a1, comment="String", protocol=i)

    @seed(9)
    @given(st.binary())
    def test_binary(self, data):
        for i in range(0, pickle.HIGHEST_PROTOCOL + 1):
            try:
                dump_a1 = dumps(data, protocol=i)
                dump_a2 = dumps(data, protocol=i)
            except PicklingError as e:
                print(f"Error in pickling: {data} - error: {e}")
                raise ValueError(f"Error in pickling: {data} - error: {e}")

            try:
                h_a1 = sha256(dump_a1).hexdigest()
                h_a2 = sha256(dump_a2).hexdigest()
            except Exception as e:
                print(f"Error in hashing: {data} - error: {e}")
                raise ValueError(f"Error in pickling: {data} - error: {e}")

            assert h_a1 == h_a2
            if logger:
                save_unpickled_test(data=h_a1, comment="Bytes", protocol=i)

    @seed(10)
    @given(st.lists(st.integers(min_value=0, max_value=255)))
    def test_bytearrays(self, data):
        c = bytearray(data)
        for i in range(0, pickle.HIGHEST_PROTOCOL + 1):
            try:
                dump_a1 = dumps(data, protocol=i)
                dump_a2 = dumps(data, protocol=i)
            except PicklingError as e:
                print(f"Error in pickling: {data} - error: {e}")
                raise ValueError(f"Error in pickling: {data} - error: {e}")

            try:
                h_a1 = sha256(dump_a1).hexdigest()
                h_a2 = sha256(dump_a2).hexdigest()
            except Exception as e:
                print(f"Error in hashing: {data} - error: {e}")
                raise ValueError(f"Error in pickling: {data} - error: {e}")

            assert h_a1 == h_a2
            if logger:
                save_unpickled_test(data=h_a1, comment="Bytearray", protocol=i)

    @seed(11)
    @given(st.tuples(st.integers(), st.floats(allow_nan=False), st.text(), st.booleans()))
    def test_tuples(self, data):
        for i in range(0, pickle.HIGHEST_PROTOCOL + 1):
            try:
                dump_a1 = dumps(data, protocol=i)
                dump_a2 = dumps(data, protocol=i)
            except PicklingError as e:
                print(f"Error in pickling: {data} - error: {e}")
                raise ValueError(f"Error in pickling: {data} - error: {e}")

            try:
                h_a1 = sha256(dump_a1).hexdigest()
                h_a2 = sha256(dump_a2).hexdigest()
            except Exception as e:
                print(f"Error in hashing: {data} - error: {e}")
                raise ValueError(f"Error in pickling: {data} - error: {e}")

            assert h_a1 == h_a2
            if logger:
                save_unpickled_test(data=h_a1, comment="Tuple", protocol=i)

    @seed(12)
    @given(st.lists(elements=one_dim_random_strategy()))
    def test_lists(self, data):
        for i in range(0, pickle.HIGHEST_PROTOCOL + 1):
            try:
                dump_a1 = dumps(data, protocol=i)
                dump_a2 = dumps(data, protocol=i)
            except PicklingError as e:
                print(f"Error in pickling: {data} - error: {e}")
                raise ValueError(f"Error in pickling: {data} - error: {e}")

            try:
                h_a1 = sha256(dump_a1).hexdigest()
                h_a2 = sha256(dump_a2).hexdigest()
            except Exception as e:
                print(f"Error in hashing: {data} - error: {e}")
                raise ValueError(f"Error in pickling: {data} - error: {e}")

            assert h_a1 == h_a2
            if logger:
                save_unpickled_test(data=h_a1, comment="List", protocol=i)


    @seed(13)
    @given(st.sets(elements=one_dim_random_strategy()))
    def test_sets(self, data):
        for i in range(0, pickle.HIGHEST_PROTOCOL + 1):
            try:
                dump_a1 = dumps(data, protocol=i)
                dump_a2 = dumps(data, protocol=i)
            except PicklingError as e:
                print(f"Error in pickling: {data} - error: {e}")
                raise ValueError(f"Error in pickling: {data} - error: {e}")

            try:
                h_a1 = sha256(dump_a1).hexdigest()
                h_a2 = sha256(dump_a2).hexdigest()
            except Exception as e:
                print(f"Error in hashing: {data} - error: {e}")
                raise ValueError(f"Error in pickling: {data} - error: {e}")

            assert h_a1 == h_a2
            if logger:
                save_unpickled_test(data=h_a1, comment="Set", protocol=i)

    @seed(14)
    @given(st.dictionaries(keys=st.text(), values=one_dim_random_strategy()))
    def test_dictionaries(self, data):
        for i in range(0, pickle.HIGHEST_PROTOCOL + 1):
            try:
                dump_a1 = dumps(data, protocol=i)
                dump_a2 = dumps(data, protocol=i)
            except PicklingError as e:
                print(f"Error in pickling: {data} - error: {e}")
                raise ValueError(f"Error in pickling: {data} - error: {e}")

            try:
                h_a1 = sha256(dump_a1).hexdigest()
                h_a2 = sha256(dump_a2).hexdigest()
            except Exception as e:
                print(f"Error in hashing: {data} - error: {e}")
                raise ValueError(f"Error in pickling: {data} - error: {e}")

            assert h_a1 == h_a2
            if logger:
                save_unpickled_test(data=h_a1, comment="Dictionary", protocol=i)

    @seed(15)
    @given(st.recursive(one_dim_random_strategy(), lambda children: st.lists(children)))
    def test_recursive_lists(self, data):
        for i in range(0, pickle.HIGHEST_PROTOCOL + 1):
            try:
                dump_a1 = dumps(data, protocol=i)
                dump_a2 = dumps(data, protocol=i)
            except PicklingError as e:
                print(f"Error in pickling: {data} - error: {e}")
                raise ValueError(f"Error in pickling: {data} - error: {e}")

            try:
                h_a1 = sha256(dump_a1).hexdigest()
                h_a2 = sha256(dump_a2).hexdigest()
            except Exception as e:
                print(f"Error in hashing: {data} - error: {e}")
                raise ValueError(f"Error in pickling: {data} - error: {e}")

            assert h_a1 == h_a2
            if logger:
                save_unpickled_test(data=h_a1, comment="Recursive List", protocol=i)

    @seed(16)
    @given(st.recursive(one_dim_random_strategy(), lambda children: st.frozensets(children)))
    def test_recursive_sets(self, data):
        for i in range(0, pickle.HIGHEST_PROTOCOL + 1):
            try:
                dump_a1 = dumps(data, protocol=i)
                dump_a2 = dumps(data, protocol=i)
            except PicklingError as e:
                print(f"Error in pickling: {data} - error: {e}")
                raise ValueError(f"Error in pickling: {data} - error: {e}")

            try:
                h_a1 = sha256(dump_a1).hexdigest()
                h_a2 = sha256(dump_a2).hexdigest()
            except Exception as e:
                print(f"Error in hashing: {data} - error: {e}")
                raise ValueError(f"Error in pickling: {data} - error: {e}")

            assert h_a1 == h_a2
            if logger:
                save_unpickled_test(data=h_a1, comment="Recursive Set", protocol=i)

    @seed(17)
    @given(st.recursive(one_dim_random_strategy(), lambda children: st.dictionaries(keys=st.text(), values=children)))
    def test_recursive_dictionaries(self, data):
        for i in range(0, pickle.HIGHEST_PROTOCOL + 1):
            try:
                dump_a1 = dumps(data, protocol=i)
                dump_a2 = dumps(data, protocol=i)
            except PicklingError as e:
                print(f"Error in pickling: {data} - error: {e}")
                raise ValueError(f"Error in pickling: {data} - error: {e}")

            try:
                h_a1 = sha256(dump_a1).hexdigest()
                h_a2 = sha256(dump_a2).hexdigest()
            except Exception as e:
                print(f"Error in hashing: {data} - error: {e}")
                raise ValueError(f"Error in pickling: {data} - error: {e}")

            assert h_a1 == h_a2
            if logger:
                save_unpickled_test(data=h_a1, comment="Recursive Dictionary", protocol=i)
    @seed(18)
    @given(st.sampled_from([add_function, is_prime, tri_recursion, get_lengths]))
    def test_functions(self, data):
        for i in range(0, pickle.HIGHEST_PROTOCOL + 1):
            try:
                dump_a1 = dumps(data, protocol=i)
                dump_a2 = dumps(data, protocol=i)
            except PicklingError as e:
                print(f"Error in pickling: {data} - error: {e}")
                raise ValueError(f"Error in pickling: {data} - error: {e}")

            try:
                h_a1 = sha256(dump_a1).hexdigest()
                h_a2 = sha256(dump_a2).hexdigest()
            except Exception as e:
                print(f"Error in hashing: {data} - error: {e}")
                raise ValueError(f"Error in pickling: {data} - error: {e}")

            assert h_a1 == h_a2
            if logger:
                save_unpickled_test(data=h_a1, comment="Function", protocol=i)
    @seed(19)
    @given(st.sampled_from([Student, Person, Temperature]))
    def test_classes(self, data):
        for i in range(0, pickle.HIGHEST_PROTOCOL + 1):
            try:
                dump_a1 = dumps(data, protocol=i)
                dump_a2 = dumps(data, protocol=i)
            except PicklingError as e:
                print(f"Error in pickling: {data} - error: {e}")
                raise ValueError(f"Error in pickling: {data} - error: {e}")

            try:
                h_a1 = sha256(dump_a1).hexdigest()
                h_a2 = sha256(dump_a2).hexdigest()
            except Exception as e:
                print(f"Error in hashing: {data} - error: {e}")
                raise ValueError(f"Error in pickling: {data} - error: {e}")

            assert h_a1 == h_a2
            if logger:
                save_unpickled_test(data=h_a1, comment="Class", protocol=i)

    @seed(20)
    @given(st.sampled_from([Student("Tobias", 21), Person("Oliver", 21), Temperature(37)]))
    def test_instances(self, data):
        for i in range(0, pickle.HIGHEST_PROTOCOL + 1):
            try:
                dump_a1 = dumps(data, protocol=i)
                dump_a2 = dumps(data, protocol=i)
            except PicklingError as e:
                print(f"Error in pickling: {data} - error: {e}")
                raise ValueError(f"Error in pickling: {data} - error: {e}")

            try:
                h_a1 = sha256(dump_a1).hexdigest()
                h_a2 = sha256(dump_a2).hexdigest()
            except Exception as e:
                print(f"Error in hashing: {data} - error: {e}")
                raise ValueError(f"Error in pickling: {data} - error: {e}")

            assert h_a1 == h_a2
            if logger:
                save_unpickled_test(data=h_a1, comment="Instance", protocol=i)

    def test_floating_point(self):
        '''Test to see how well the pickle handles extreme floatingpoint accuracy'''
        getcontext().prec = 309
        a = Decimal(2)**Decimal(0.5)
        b = Decimal(2.2250738585072014e-308)
        c = a+b
        c1 = dumps(a)
        s1 = sha256(c1).hexdigest()

        c2 = dumps(c)
        s2 = sha256(c2).hexdigest()

        assert s1 != s2

if __name__ == '__main__':
    clean_folder()
    pytest.main()
