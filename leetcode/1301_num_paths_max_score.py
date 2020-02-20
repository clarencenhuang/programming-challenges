'''
use 2 dp series to model this

# max_value
dp_max[i][j] = max( dp_max[i_reachable][j_reachable]) + my_value)

dp_ways[i][j][k] = dp_ways[i_reachable][j_reachable][k - my_value]

'''
import functools

to_mod = 10**9 + 7
def num_path_max(board):
    nrows, ncols = len(board), len(board[0])
    dirs = (
        (1,  0),
        (0,  1),
        (1, 1)
    )

    def prev_reachable(i, j):
        for ii, jj in dirs:
            ni = i + ii
            nj = j + jj
            if (0 <= ni < nrows and
                    0 <= nj < ncols and
                    board[ni][nj] != 'X'):
                yield (ni, nj)

    @functools.lru_cache(None)
    def dp_max(i, j):
        if board[i][j] == 'S':
            return (0, 1)
        val = 0 if board[i][j] == 'E' else int(board[i][j])
        prev_vals = [dp_max(ii, jj) for ii, jj in prev_reachable(i, j) if dp_max(ii, jj)[0] >= 0]
        if not prev_vals:
            return (-1, 0)
        max_pv = max(prev_vals)[0]
        num_ways = sum([pv[1] for pv in prev_vals if pv[0] == max_pv])
        return val + max_pv, num_ways % to_mod
    res = dp_max(0, 0)
    if res[0] == -1:
        res = [0, 0]
    return res

if __name__ == '__main__':
    print(num_path_max([
  "E81214XX563827518571147861868X9X28X4291233941511X83848128X9778953222X96X11549365313X6598352872184791",
  "5X27194843691X8526257741281758X54X2684658512X6692536397XXXX81955612886913735611538X6781X712257289X81",
  "66484441453X3497754817929873X48448X51447857649661881X46625542846X29333X272X8X69393X328178X74X4122316",
  "79X2X81XX559674472567694X12341241284843929XX43777229356828878844775476363X58482349698674X85532756958",
  "18418511334559843753XX3982715X5663394716X41135737X4928429369579355117283121214888976314911XX9389X574",
  "X114113X489625X955X14X978892247293781X881138546X415X53X69555XX8783131753159464165936642658361848135X",
  "94467333442X2X99723919499933X9X29452X3X29388212396X36747X517X6XX7887196215934X8812657935988695994864",
  "44X9655767592398447X55353X35632X7X8113X868235959559XX5X1397453295612178669859477297994768216497227X8",
  "466312X78242319827313824989X21665297636XX467X31X2X3319756964392722539867X623478195871264629933X71711",
  "88537698421895539278X854247X3784592X71821618318292X25594178X2374487742779835363791165722646X469648X8",
  "534X273341744X137X9957657X684481777419386246411X279697X73312519717637X897X593X23X3974885XXX221X21416",
  "5749X285835174612724964934311234988685X912941647144186X24X9X3866763X49914967188788916663371793796173",
  "2X7998617X79627342616762773X7947148X9348361882542276476544638X618468XX2771632193X9X41256X887551XX723",
  "75269787X312676898X5296111628737X75258249432XX7764926216825142462533X62947176694397921X7538345618994",
  "87876X32521391X724987849828214X49415252636997682515662969XX277627874258664X49936831475516788X112551X",
  "94623522X14X56689822X4837X821152418X62X17X8X256X16675926888886986931886173957X713X37245226763862673X",
  "X3X266565858X29843XXX5456938278551381435X64X172176X691911727X9868868X712X763582X4185X4816X892478559X",
  "2757356914256945994X94X29921615511768667625294129498226923869346X5359X363644983331X2X73284514X219212",
  "6323X4218X1779183925X622291X54142998X8874474493993872189721XX58253X941X48847827489477779497722834476",
  "27393233892631X32X86664887173537537596549X812978X7X81361455X22737X215X8311646179656855X754453X341344",
  "484946557924866X67113676212497X71789543718571734X78274154736X2127X967164641676X593562117839594113368",
  "4296X54748X361413X73685586X19135152118X51436426175X1XX355X555X231X887547539X7484595649417744418721X9",
  "X1713829X11X292737X25367936376622218718897981355X56669626198246313X3433793645716445549268284X9XX3927",
  "84789357194334318273X585328685725181977X66836X4656X593329414376696352X442593X2889X567318946386349646",
  "47X3752X75X83335584567235748715417225622371439542582X7X9859339223498918547X921171XX78258242693175444",
  "63565X673164329993XX61573825331475X412X156X2535X16572529291787543855337333197863X82462311X8666992141",
  "76116382317193239347X681798575597X96X628652754X386XX6361865X127443458648345XX12158X5X233941X38618225",
  "521763618X9796684411365544127328143493115X274168381X492835732848433X8X4566449X536952748X112644513X3X",
  "X4X254X49231X6188587412337X475565583X9286XX2552227X59XX23158296173674XX3X217X38631X356X6257464629319",
  "X212413677X717267723781XX66X482233749566852551812X45783715914X17356X8561X38954X9346731X5272528727415",
  "1625985X5X42368X1X221419544111X9428482567891498749299311396537X59839246688X433X975922224971393X58252",
  "X72639X28545X3993224784597676XX9X749889471X8647339431833699X68889472115X2XX94184X356755976157745X546",
  "294853329XX925449X825858345X5X5X4999457841217815514X98339188559316187XX43632852814672X4599X586142237",
  "8X8879219838155112X6623432556X214856796211X32387445662959956325763X149339611878733323563529825535X78",
  "398X148546959292647X6X98X3134636X65X176X143726X588716XX686X87765826X49299X63288925193569X458X5786979",
  "543X84X9259653X9726293393X56918735752887X79446772859867X46665998X488721886773343X7589693168689268137",
  "13266X795X42518221468658882972X58361353755785524178147871XX4944989588728X2734X63X3995849936332849214",
  "14461868X258X7383216771999616428767546X85513452635943824781777522149683155274X3535X7X674782X26816832",
  "525533521448441686957X12257X7229692145225673554363438711849639283275591XX49976X2X79522313X43991485X2",
  "65468X2931X57298XX73792435879X9342789237855425X29574439648X61X1184X31346X18X953853631247919X84894457",
  "X9839872132335863472312367895597534182676853X97X63639628267354812256545X977888451748X385695513845396",
  "X3413X4622X9993751776542893X317586X8X5XX37447X744X866X5987859489X6716537145618517982X396X148351647XX",
  "99677828662564814X7X372965925236986159157563239XX2389X3445734631164658954563336832256895637932998787",
  "843968692921654786432261211694656446428627143994221328135331868X22541818958X4729X319534992666557567X",
  "933XX997767579583611648397X917X54791291569644X89XX9X6721X55991XX184679754847265X2X63153957321X537846",
  "7861172656X274683776165121762117471175618213189754544X25438583488X19X8X5X52XX648XX244164959393787478",
  "65222815664447X5138X917442716XX5XX55546133916269X33696367XXX4245XX18X9482847X693485798356XX4169977X4",
  "71745992842161821961862738X4794642152X6529956564443XX679626X2985X315X67938754699947144XX323X46882929",
  "5325637131X22X1643294662X7152511818658XX2179XX957629129X1X82985164718932563224369X442732434117X88296",
  "9357X8X8248462X8736477679967272459X68886297X77X26187X6176818351797599XX39259X44X626187616774X7X186X9",
  "78195427416215X6276X2XX12524X885X249163X81155445764851393633946X3X54515777X8568767724282915155973731",
  "88574633619X132885176453X2446199697X8695534964983559864898X2319X66X734X27282XX5634141913473888X76261",
  "8322884128992X736674251X4361387X56892585656844231X23464749699817455417132299387891775X84221516348869",
  "X136X256426545587498X59X73235653692995946X1875365X782829XX9337X9X97625545449737662959456124746771656",
  "228X47549262448974X381962282866X13752X619813864X936371555X92X85797554X451311515335341X12X5712X993442",
  "73528539998225978X1575354165935X4457X3266227547366436X711537X785X6X552357X526988393X551785X1991875X5",
  "8292X49788924878XXX39255X6649663515392239515343X271873638783X53X983393422X684967599X2X35X48163824493",
  "451922784773X725986X884X548X6321242629269474X84X844X9225645335488878619973745669X34551446X4X8X6897X8",
  "36X58133574X6576484498322X73292522X44721X213314X34124669773X834573996316248685X43X346498373381863X28",
  "73687X7561917894297736X7X5934189X193X45993868582X968X16659X42461494639534497X81782591264X196XX643916",
  "4X97155674427185982154822784536459721682198X528997632458686332X86214695173X2498X39195715917176X65795",
  "395932348756439521X65966738657X9479X4385737121768578X2X598555X92288926939774537X83575498679931376937",
  "48X218576258756621X8338423322812X5696598788134168295577X86596199471474X9352533628393422331X571155955",
  "9X274177493839188477337828471X86X68847273X194X64619X738664535679784X4682X96225X5461666X7187713769751",
  "5176X6XXX66768XX1454XX8346X73XX8968535749641X127X743X97165887464X79888852496283146337985195X83164612",
  "561429862X98248X467581494528834224638855987X38X42XX3545X4839173X61X1465X4164744893X9XX39848292254262",
  "74445X7581376783261897548842874549842865492X81583592X633842XX61348348511X21174879X964424X429671X92X2",
  "3125877648576X3912X87763721775X84127764426135X3152912X4351X825494X573378X1X54659624482941X9256282216",
  "21X79649569729X85134XX5X773274466924X443968877531523X468824599X786715216337323747615132672X965358721",
  "3591475X9929119464XX9317793279XX67X272995X185XX1925462546696X9X741685X7473X75X7X479X5523858X1843XX55",
  "4885269X212655548X8797549934394395693492X587748229514XX19493786X935954397576867321246389892623914X56",
  "64754299132587X699667773942X867327X75375645271X1X987983X3453XX6793749164585945498XX95169622159165638",
  "4538382941827915227X62577XX2428X649434X5548449862295X978267998133254196X68473679471872212232258XXX93",
  "8672861986298364X95219519557549315475X2575316734338638237472678647218362661936341654958322113397XX7X",
  "2X161465148499645X91211X75895931X7864X232795X8728549631269833232418444X457646572X3676549X56X57639551",
  "54468199457621X472686X23X2677X9932X67625943242X4X644353X4X655XX9X4423711119X196X3X3934X696472X852XX7",
  "5917969923X3X816X62X988883191971724774215X92621986588538829534X5219XX66XX255159599719636146X2184X338",
  "213591978338563XX382178695691933795864X5591624X7453X6682745X72427813914936163112X875451X8535216X6677",
  "73579283X6X1644X553653856X6926513X4XXX15X946X54623793667715685684X9596416X4515196X48X68793922X497233",
  "26416619836668X646X9788X8657648XX1394716647X73372628545X432227431711X224718295915668X24XX87789354X21",
  "44X3X1978X597XX3299863168353695148278535737642283553986397161X61878X9X1251485X214471333X5X8755564126",
  "717184928887X6769683269289X939657544X5353946125235789146971826277421644294122241152526X533594X1X1X98",
  "364X6X661862582942289589214962X4964161759X52884X343423883442657X7948682X4251695633266872348X51X4476X",
  "36811918XX673543856628571447839166X825X84985XX668215X76281971XX499X2XX1789X4526734413X44274272761867",
  "987567263789947113878528217851719892X73454X9458488961253795424X1XX37X484618X4778295236872237398992X3",
  "84436184X45781X7517366X6637915498535491316634X87859784399X97X9754584628732889X72534595933335516X9682",
  "1489464446546391543481823541674X75292771392823185X7X7679949565459832X967992233464545962384646X93X994",
  "1496358448633771X41992765XXX2655891X318689511XX6217861634984967482832886799X51X1433677589X5XX2752214",
  "X23194X6542X784832627854992633157XX9676X194598985633471396396X54883813388313631259792X367XX73689X97X",
  "97547725X3221X639X5215451X91941984827X62499741X172X884623X9995865434767871734561639765276451X387XX59",
  "678859544384X72X3XX3484119739456395886938696129298183951897562358857X7895293958X1327167521348671X58X",
  "12334166419516944XX9X4625756X6X6527894X84179243655X614X1893613X51317528X48758437477X3532534442829268",
  "843925447781X453359616X769619674212271X8X21834838425612846532698835827747716536X5535314121741X489X2X",
  "87241852XX526799981XX8X6X42X8988681534142161541541946X7657242643X88958XXX221X42X34X38711172264673466",
  "53X88177322714XX2X3226571791686759X12551837735665465639318X26385X98481X411629186996943615X57X811XXX8",
  "989X6483946324318323X379XX18527528943761162795163686472X7X286164446X8X9X26X9694715X7678X5X1529323353",
  "39876X7541943664X4296196951648592X734331694613X19525217484X945726278594511189423X7X193331531X5269985",
  "54X6219152484632X3876336585841464X55268X5X2X226724114239835XX5335479252578533394751377262X7393432875",
  "2X3279873955866475X1834626X381195637675987264199492379396411X954443X93468538652412735813266938227XX1",
  "6X376252192X71547227X68139X48788324663X853682915X84318132942714666X5543717XX6X997X95181XX6675595424S"
]))



