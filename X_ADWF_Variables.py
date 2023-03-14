##AFTER UPDATE AND SAVE YOU MUST RESTART THE KERNEL IN JUPYTER NOTEBOOK TO UPDATE VARIABLES!

##Remember to insert r in front of all paths, e.g. r"J:\SEWER_AREA_MODELS\FSA\03_SIMULATION_WORK\Calibration_2022\MODEL"


#FSA
wwtp_pipe = '52458'
specs = []

specs.append([3,'FSA_Base_2020pop_V050_3xADWF.mdb','FSA_3ADWF_2020pop_Base.res1d','Annacis',''])
specs.append([3,'FSA_Base_2030pop_V050_BurnabyLake_3xADWF.mdb','FSA_3ADWF_2030pop_BurnabyLake.res1d','Annacis',''])
specs.append([3,'FSA_Base_2040pop_V050_BurnabyLake_3xADWF.mdb','FSA_3ADWF_2040pop_BurnabyLake.res1d','Annacis',''])
specs.append([3,'FSA_Base_2050pop_V050_BurnabyLake_3xADWF.mdb','FSA_3ADWF_2050pop_BurnabyLake.res1d','Annacis',''])
specs.append([3,'FSA_Base_2060pop_V050_BurnabyLake_3xADWF.mdb','FSA_3ADWF_2060pop_BurnabyLake.res1d','Annacis',''])

df_theory_sheet = r"J:\SEWER_AREA_MODELS\FSA\04_ANALYSIS_WORK\System_Assessment\System_Assessment_Mapping\FSA_XADWF_Internal\Theory_ADWF.xlsx"
result_folder = r"J:\SEWER_AREA_MODELS\FSA\03_SIMULATION_WORK\Port_Coquitlam_PS_VFD\Model_3ADWF"
map_folder = r"J:\SEWER_AREA_MODELS\FSA\04_ANALYSIS_WORK\System_Assessment\System_Assessment_Mapping\FSA_XADWF_Internal"
dwf_file_path = r"J:\SEWER_AREA_MODELS\FSA\03_SIMULATION_WORK\Allways_Latest_Master_Model_Simulations\Model\FSA_DWF_2021-07-23_4d_2020pop_Base.res1d"
runoff_results = [] #Must be in order, smallest return period at top
runoff_results.append([2,'FSA_Runoff_EX-2yr-24hr-AES_BaseRR.res1d'])
runoff_results.append([5,'FSA_Runoff_EX-5yr-24hr-AES_BaseRR.res1d'])
runoff_results.append([10,'FSA_Runoff_EX-10yr-24hr-AES_BaseRR.res1d'])
runoff_results.append([25,'FSA_Runoff_EX-25yr-24hr-AES_BaseRR.res1d'])
runoff_results.append([50,'FSA_Runoff_EX-50yr-24hr-AES_BaseRR.res1d'])
runoff_results.append([100,'FSA_Runoff_EX-100yr-24hr-AES_BaseRR.res1d'])
runoff_results.append([200,'FSA_Runoff_EX-200yr-24hr-AES_BaseRR.res1d'])


# #FSA
# wwtp_pipe = '52458'
# specs = []
# specs.append([2.5,5.886,'FSA_2p5ADWF_2020pop_Base.res1d','Annacis',''])
# specs.append([3,8.607,'FSA_3ADWF_2020pop_Base.res1d','Annacis',''])
# specs.append([4,14.050,'FSA_4ADWF_2020pop_Base.res1d',"Annacis",''])

# specs.append([2.5,5.886,'FSA_2p5ADWF_2020pop_VFD_Base.res1d','Annacis','VFD'])
# specs.append([3,8.607,'FSA_3ADWF_2020pop_VFD_Base.res1d','Annacis','VFD'])
# specs.append([4,14.050,'FSA_4ADWF_2020pop_VFD_Base.res1d',"Annacis",'VFD'])
# specs.append([5,19.492,'FSA_5ADWF_2020pop_VFD_Base.res1d',"Annacis",'VFD'])

# df_theory_sheet = r"J:\SEWER_AREA_MODELS\FSA\03_SIMULATION_WORK\Threes_Times_ADWF\Model\SA_Maps\Theory_ADWF.xlsx"
# result_folder = r"J:\SEWER_AREA_MODELS\FSA\03_SIMULATION_WORK\Threes_Times_ADWF\Model"
# map_folder = r"J:\SEWER_AREA_MODELS\FSA\03_SIMULATION_WORK\Threes_Times_ADWF\Model\SA_Maps"
# dwf_file_path = r"J:\SEWER_AREA_MODELS\FSA\03_SIMULATION_WORK\Allways_Latest_Master_Model_Simulations\Model\FSA_DWF_2021-07-23_4d_2020pop_Base.res1d"
# runoff_results = [] #Must be in order, smallest return period at top
# runoff_results.append([2,'FSA_Runoff_EX-2yr-24hr-AES_BaseRR.res1d'])
# runoff_results.append([5,'FSA_Runoff_EX-5yr-24hr-AES_BaseRR.res1d'])
# runoff_results.append([10,'FSA_Runoff_EX-10yr-24hr-AES_BaseRR.res1d'])
# runoff_results.append([25,'FSA_Runoff_EX-25yr-24hr-AES_BaseRR.res1d'])
# runoff_results.append([50,'FSA_Runoff_EX-50yr-24hr-AES_BaseRR.res1d'])
# runoff_results.append([100,'FSA_Runoff_EX-100yr-24hr-AES_BaseRR.res1d'])
# runoff_results.append([200,'FSA_Runoff_EX-200yr-24hr-AES_BaseRR.res1d'])


# #NSSA
# wwtp_pipe = '54959_a'
# specs = []
# specs.append([3,'NSSA_Base_2018pop_V062_3xADWF.mdb','NSSA_3ADWF_2018pop_Base.res1d',"Lion's Gate",''])
# specs.append([3.5,'NSSA_Base_2018pop_V062_3p5xADWF.mdb','NSSA_3p5ADWF_2018pop_Base.res1d',"Lion's Gate",''])
# specs.append([4,'NSSA_Base_2018pop_V062_4xADWF.mdb','NSSA_4ADWF_2018pop_Base.res1d',"Lion's Gate",''])
# specs.append([5,'NSSA_Base_2018pop_V062_5xADWF.mdb','NSSA_5ADWF_2018pop_Base.res1d',"Lion's Gate",''])

# specs.append([3,'NSSA_Base_2018pop_V062_3xADWF.mdb','NSSA_3ADWF_2018pop_V_Base.res1d',"Lion's Gate",'VFD'])
# specs.append([3.5,'NSSA_Base_2018pop_V062_3p5xADWF.mdb','NSSA_3p5ADWF_2018pop_V_Base.res1d',"Lion's Gate",'VFD'])
# specs.append([4,'NSSA_Base_2018pop_V062_4xADWF.mdb','NSSA_4ADWF_2018pop_V_Base.res1d',"Lion's Gate",'VFD'])
# specs.append([5,'NSSA_Base_2018pop_V062_5xADWF.mdb','NSSA_5ADWF_2018pop_V_Base.res1d',"Lion's Gate",'VFD'])

# df_theory_sheet = r"J:\SEWER_AREA_MODELS\NSSA\03_SIMULATION_WORK\X-ADWF\Model\X-ADWF_Diurnals.csv" # < Full path to X-ADWF_Diurnals.csv in your local exercise folder.
# deficits_csv = r"J:\SEWER_AREA_MODELS\NSSA\03_SIMULATION_WORK\X-ADWF\Model\Deficits.csv"
# result_folder = r"J:\SEWER_AREA_MODELS\NSSA\03_SIMULATION_WORK\X-ADWF\Model" # < Full path to the model folder in your local exercise folder.
# map_folder = r"J:\SEWER_AREA_MODELS\NSSA\03_SIMULATION_WORK\X-ADWF\Model\SA_Maps_Int" # < Full path to the Model\SA_ Maps folder in your local exercise folder.
# dwf_file_path = r"J:\SEWER_AREA_MODELS\NSSA\03_SIMULATION_WORK\X-ADWF\Model\NSSA_DWF_2018-07-26_4d_2018pop_Base.res1d" #Leave as is
# runoff_results = [] #Must be in order, smallest return period at top
# runoff_results.append([2,'NSSA_Runoff_EX-2yr-24hr-AES_BaseRR.res1d'])
# runoff_results.append([5,'NSSA_Runoff_EX-5yr-24hr-AES_BaseRR.res1d'])
# runoff_results.append([10,'NSSA_Runoff_EX-10yr-24hr-AES_BaseRR.res1d'])
# runoff_results.append([25,'NSSA_Runoff_EX-25yr-24hr-AES_BaseRR.res1d'])
# runoff_results.append([50,'NSSA_Runoff_EX-50yr-24hr-AES_BaseRR.res1d'])
# runoff_results.append([100,'NSSA_Runoff_EX-100yr-24hr-AES_BaseRR.res1d'])
# runoff_results.append([200,'NSSA_Runoff_EX-200yr-24hr-AES_BaseRR.res1d'])