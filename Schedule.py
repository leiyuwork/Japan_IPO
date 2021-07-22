import pandas as pd  # excel data操作要パッケージを導入
import time

for i in ["1382", "1383", "3352", "3353", "3356", "3358", "3359", "3361", "3362", "3364",
          "3366", "3367", "3370", "3371", "3372", "3373", "3374", "3375", "3376", "3377", "3379", "3381", "3383",
          "3384", "3385", "3386", "3387", "3388", "3390", "3393", "3394", "3397", "3399", "3415", "3416", "3418",
          "3419", "3435", "3437", "3439", "3440", "3441", "3444", "3445", "3446", "3452", "3454", "3457", "3461",
          "3464", "3467", "3469", "3474", "3475", "3477", "3479", "3482", "3484", "3486", "3489", "3490", "3491",
          "3494", "3495", "3496", "3497", "3498", "3537", "3538", "3540", "3541", "3542", "3545", "3547", "3550",
          "3556", "3557", "3558", "3559", "3560", "3561", "3562", "3565", "3566", "3620", "3622", "3623", "3624",
          "3625", "3627", "3628", "3629", "3632", "3633", "3634", "3639", "3641", "3644", "3645", "3646", "3649",
          "3652", "3653", "3654", "3655", "3656", "3657", "3658", "3660", "3661", "3662", "3664", "3665", "3666",
          "3667", "3668", "3669", "3670", "3671", "3672", "3674", "3677", "3678", "3679", "3680", "3681", "3682",
          "3683", "3685", "3686", "3687", "3688", "3689", "3690", "3691", "3692", "3694", "3695", "3696", "3697",
          "3698", "3710", "3712", "3714", "3715", "3716", "3720", "3722", "3723", "3724", "3727", "3730", "3731",
          "3732", "3733", "3734", "3736", "3739", "3740", "3742", "3744", "3745", "3746", "3747", "3749", "3751",
          "3753", "3755", "3756", "3758", "3760", "3762", "3763", "3764", "3765", "3766", "3767", "3768", "3769",
          "3770", "3771", "3772", "3773", "3775", "3776", "3777", "3778", "3780", "3781", "3782", "3783", "3784",
          "3785", "3786", "3787", "3788", "3789", "3790", "3791", "3792", "3793", "3794", "3796", "3797", "3798",
          "3799", "3800", "3801", "3802", "3803", "3804", "3807", "3808", "3809", "3810", "3811", "3812", "3813",
          "3814", "3815", "3816", "3818", "3821", "3822", "3823", "3824", "3825", "3826", "3827", "3829", "3830",
          "3831", "3832", "3835", "3836", "3837", "3838", "3839", "3840", "3841", "3842", "3843", "3844", "3845",
          "3846", "3847", "3848", "3849", "3850", "3851", "3852", "3853", "3854", "3856", "3858", "3859", "3895",
          "3900", "3901", "3902", "3904", "3905", "3906", "3907", "3908", "3909", "3910", "3911", "3912", "3913",
          "3914", "3915", "3916", "3917", "3918", "3920", "3921", "3922", "3923", "3925", "3926", "3927", "3928",
          "3929", "3930", "3931", "3932", "3933", "3934", "3935", "3936", "3937", "3939", "3940", "3960", "3961",
          "3962", "3963", "3965", "3966", "3967", "3968", "3969", "3970", "3974", "3976", "3977", "3979", "3981",
          "3983", "3984", "3985", "3986", "3987", "3988", "3989", "3990", "3991", "3992", "3993", "3994", "3995",
          "3996", "3997", "3998", "3999", "4124", "4237", "4238", "4239", "4240", "4241", "4242", "4243", "4244",
          "4280", "4281", "4287", "4288", "4289", "4290", "4293", "4296", "4300", "4301", "4302", "4303", "4304",
          "4305", "4308", "4309", "4310", "4313", "4314", "4316", "4317", "4320", "4321", "4322", "4327", "4330",
          "4331", "4332", "4334", "4335", "4336", "4344", "4346", "4347", "4350", "4351", "4352", "4355", "4356",
          "4357", "4369", "4380", "4381", "4382", "4384", "4385", "4386", "4387", "4388", "4389", "4390", "4391",
          "4393", "4394", "4395", "4396", "4397", "4398", "4420", "4421", "4422", "4424", "4425", "4427", "4428",
          "4429", "4431", "4434", "4435", "4436", "4437", "4438", "4439", "4440", "4441", "4442", "4443", "4444",
          "4445", "4446", "4447", "4448", "4449", "4450", "4475", "4476", "4477", "4478", "4479", "4480", "4482",
          "4483", "4484", "4485", "4486", "4487", "4488", "4563", "4564", "4565", "4566", "4567", "4570", "4571",
          "4572", "4573", "4575", "4576", "4579", "4582", "4583", "4584", "4585", "4586", "4587", "4588", "4589",
          "4591", "4697", "4740", "4741", "4744", "4747", "4749", "4751", "4753", "4756", "4759", "4762", "4763",
          "4764", "4765", "4766", "4770", "4771", "4772", "4773", "4776", "4777", "4779", "4784", "4786", "4787",
          "4788", "4789", "4791", "4792", "4794", "4795", "4797", "4798", "4800", "4809", "4813", "4814", "4815",
          "4817", "4818", "4821", "4822", "4824", "4825", "4827", "4829", "4830", "4831", "4833", "4838", "4839",
          "4840", "4841", "4842", "4845", "4849", "4875", "4880", "4925", "4926", "4952", "4971", "4974", "4976",
          "5456", "5724", "5742", "5758", "6038", "6050", "6051", "6052", "6054", "6058", "6059", "6060", "6061",
          "6062", "6063", "6064", "6065", "6067", "6156", "6159", "6160", "6161", "6163", "6164", "6253", "6254",
          "6255", "6256", "6257", "6258", "6259", "6260", "6261", "6263", "6264", "6519", "6553", "6554", "6555",
          "6556", "6557", "6558", "6560", "6561", "6562", "6563", "6565", "6567", "6568", "6572", "6573", "6574",
          "6575", "6577", "6578", "6579", "6580", "6597", "6616", "6618", "6619", "6626", "6627", "6630", "6634",
          "6635", "6636", "6637", "6638", "6640", "6656", "6657", "6658", "6659", "6660", "6661", "6662", "6667",
          "6668", "6670", "6672", "6677", "6694", "6696", "6697", "6698", "6721", "6726", "6731", "6732", "6734",
          "6739", "6750", "6769", "6777", "6778", "6786", "6790", "6829", "6836", "7033", "7034", "7035", "7036",
          "7037", "7038", "7039", "7041", "7042", "7043", "7044", "7045", "7046", "7047", "7048", "7049", "7050",
          "7057", "7058", "7059", "7060", "7061", "7062", "7063", "7064", "7066", "7067", "7068", "7069", "7071",
          "7072", "7073", "7074", "7076", "7077", "7078", "7079", "7080", "7148", "7157", "7172", "7175", "7183",
          "7185", "7187", "7191", "7192", "7213", "7217", "7311", "7314", "7320", "7323", "7325", "7326", "7589",
          "7649", "7671", "7674", "7676", "7678", "7682", "7683", "7685", "7707", "7708", "7709", "7717", "7725",
          "7748", "7749", "7760", "7772", "7773", "7774", "7776", "7777", "7779", "7781", "7782", "7800", "7803",
          "7804", "7805", "7806", "7807", "7808", "7809", "7810", "7812", "7813", "7816", "7818", "7819", "7823",
          "7824", "7826", "7827", "7828", "7829", "7830", "7833", "7834", "7835", "7836", "7837", "7838", "7847",
          "7849", "7853", "8187", "8410", "8423", "8426", "8437", "8462", "8473", "8626", "8627", "8629", "8697",
          "8699", "8704", "8708", "8709", "8711", "8715", "8728", "8732", "8734", "8735", "8767", "8769", "8771",
          "8774", "8783", "8787", "8789", "8798", "8885", "8888", "8889", "8890", "8893", "8898", "8903", "8909",
          "8912", "8914", "8919", "8922", "8924", "8925", "8929", "8935", "8936", "8937", "8938", "8940", "8941",
          "8942", "8943", "8944", "8945", "8946", "8947", "8948", "8991", "8992", "8993", "8996", "8997", "8998",
          "9029", "9204", "9262", "9264", "9266", "9270", "9271", "9272", "9279", "9325", "9375", "9376", "9378",
          "9379", "9381", "9385", "9386", "9399", "9416", "9417", "9418", "9419", "9421", "9423", "9424", "9425",
          "9427", "9428", "9443", "9444", "9445", "9446", "9450", "9466", "9467", "9514", "9517", "9519"]:
    try:
        print(i)
        url = "https://minkabu.jp/stock/" + str(i) + "/ipo"
        dfs = pd.read_html(url)
        # print(len(dfs))
        table = dfs[2]
        Result = pd.DataFrame(table)
        Result.to_csv(r"C:\Users\Ray94\OneDrive\Research\PHD\Research\data\japan_IPO\\" + str(i) + "_引受証券会社.csv", mode='a',
                      index=False, header=None, encoding="utf-8_sig")
        time.sleep(3)
    except Exception as e:
        Error = pd.DataFrame([[str(i), str(e)]])
        Error.to_csv(r"C:\Users\Ray94\OneDrive\Research\PHD\Research\data\japan_IPO\error_引受証券会社.csv", mode='a', index=False, header=None,
                     encoding="utf-8_sig")
        pass

