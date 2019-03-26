#Alejandro Armas

def exam2_num1() :
    α_w = 69e-6 #1/°C coefficient of linear expansion
    α_c = 17e-6 #1/°C coefficient of linear expansion

    water_vol = 50 * (1e-2)**3 #meters cube
    water_den = 998 #kg/m^3
    copp_den = 8960 #kg/m^3

    c_water = 4187 # J/kg*K
    c_copp = 385 #J/kg*K

    t_init = 20 + 273.15 #Kelvin
    t_heat = 140 + 273.15 #Kelvin

    beak_rad = 2.2e-2 #meters
    rod_rad = 1.41e-2 #meter
    rod_len = 11e-2 #meter

    #*******
    print ("Part (a")
    #*******

    copp_area = math.pi * rod_rad ** 2 
    copp_vol = copp_area * rod_len
    copp_mass = copp_den * copp_vol

    water_mass = water_den * water_vol

    t_equilibrium = (copp_mass * c_copp * t_heat + 
                     water_mass * c_water * t_init ) / (copp_mass *c_copp + water_mass * c_water)

    print("The temperature of water at equilibrium is: ", t_equilibrium, "Kelvin")

    #*******
    print ("Part (b")
    #*******

    water_area_init = math.pi * beak_rad ** 2 - math.pi * rod_rad ** 2
    water_height_init = water_vol / water_area_init

    Δrod_len = rod_len * α_c * (t_equilibrium - t_init)
    rod_len_final = Δrod_len + rod_len

    copp_vol_final = copp_vol * (1 + 3 * α_c * (t_equilibrium - t_init))
    copp_area_final = copp_vol_final / rod_len_final

    water_vol_final = water_vol * (1 + 3 * α_w * (t_equilibrium - t_init))
    water_height_final = water_vol_final / (math.pi * beak_rad **2 - copp_area_final) 

    change_diff = rod_len_final - water_height_final + water_height_init - rod_len
    
    print("Change in difference of height is: ", change_diff *1e2, "cm")

def exam2_num2() : 
    k_cu = 401 # W/ m*K
    k_al = 237 # W/ m*K
    d = 0.86e-2 #meter
    l = 3.89e-2 #meter
    t1 = 5 + 273.15
    t2 = 81 + 273.15


    #*******
    print ("Part (a")
    #*******

    Δcu = (t2 - t1 ) / (1 + k_cu/k_al)
    Δal = k_cu/k_al * Δcu

    print("The change in temperature across Copper = ", Δcu , "C°")
    print("The change in temperature across Aluminum = ", Δal, "C°" )

    #*******
    print ("Part (b")
    #*******

    d_alum = (k_cu / k_al * d ** 2)** (1/2)

    print("The diameter of the rod of aluminum to be at same ΔT ", d_alum, " meters")

    #*******
    print ("Part (c")
    #*******

    Δz = 21 #C°

    Δcu = (t2 - t1 - Δz) / (1 + k_cu/k_al)
    
    k_z = k_cu / Δz * Δcu
    
    print("The thermal conductivity of unknown material is ", k_z, "W/ m*K")
    
def exam2_num3() :

    def density_vs_altitude(height_meters) :
        return float(1.2 - 1.33e-4 * height_meters) #kg / m^3
    def pressure_vs_altitude(height_meters) :
        return float( (80.7 - 101.3)*1e3 / (1800) * height_meters + 101300.) #Pa
    
    density_surr = 1.155 #kg/m^3

    c_v = 5 / 2 * gas_constant #diatomic gas 
    c_p = 7 / 2 * gas_constant
    γ = c_p / c_v

    num_moles = 1

    v_i = 23.27e-3 # m^3
    t_i = 20 + 273.15 #kelvin

   
    #*******
    print ("Part (a")
    #*******

    p_i = num_moles * gas_constant * t_i / v_i
    p_f = pressure_vs_altitude(600)

    v_f = ( (p_i * v_i ** γ )  / p_f ) ** (1. / γ)

    t_f = (v_i / v_f ) ** ( γ - 1) * t_i

    print("Air mass temperature at 600m above sea level: ", t_f, " Kelvin")

    #*******
    print ("Part (b")
    #*******

    den_f = density_vs_altitude(600)
    print("Air mass density at 600m above sea level: ", den_f, " Kg/m^3")

    #*******
    print ("Part (c")
    #*******

    p_i = num_moles * gas_constant * t_i / v_i
    p_f = pressure_vs_altitude(1200)

    v_f = ( (p_i * v_i ** γ )  / p_f ) ** (1. / γ)

    t_f = (v_i / v_f ) ** ( γ - 1) * t_i

    print("Air mass temperature at 1200m above sea level: ", t_f, " Kelvin")

    #*******
    print ("Part (d")
    #*******

    height = ((density_surr - 1.2) / -1.33e-4) #meters

    print("The air mass is expected to stop rising at: ", height, " meters")

    #*******
    print ("Part (e")
    #*******

    p_i = num_moles * gas_constant * t_i / v_i
    p_f = pressure_vs_altitude(1000)

    v_f = ( (p_i * v_i ** γ )  / p_f ) ** (1. / γ)

    t_f = (v_i / v_f ) ** ( γ - 1) * t_i

    print("The approximate change in temperature for an air mass per 1000m is: ", t_f - t_i, "C°")

def exam2_num4() :
    t_a = 464 #K #change this
    t_b = t_a #K

    p_a = 210e3 #Pa #change this
    p_c = 80e3 #Pa #change this?
    p_d = p_c #Pa

    v_a = 0.10 #m^3 #change this
    v_b = 0.15 #m^3 #change this
    v_d = v_a #m^3

    c_v = 5 / 2 * gas_constant #for diatomic gas
    c_p = 7 / 2 * gas_constant #for diatomic gas
    γ = c_p / c_v

    #*******
    print ("Part (a")
    #*******

    num_mol = p_a * v_a / ( gas_constant * t_a )

    print ("The amount of moles in gas: ",num_mol)

    #*******
    print ("Part (b")
    #*******

    p_b = p_a * v_a / v_b

    v_c = ( (p_b * v_b ** γ) / p_c)**(1./γ)

    t_c = t_b * (v_b / v_c) ** (γ - 1)
    t_d = p_d * t_a / p_a 

    
    print ("Temperature at point c is: ", t_c, "Kelvin")
    print ("Temperature at point d is: ", t_d, "Kelvin")

    #*******
    print ("Part (c")
    #*******

    w_ab = num_mol * gas_constant * t_a * math.log(v_b / v_a)
    q_ab = w_ab #isothermal
    ΔE_ab = 0 #isothermal

    w_bc = p_b * v_b ** γ * (v_c ** (1 - γ ) - v_b ** (1 - γ ) ) / (1 - γ)
    q_bc = 0 # adiabatic
    ΔE_bc = q_bc - w_bc

    w_cd = p_c * (v_d - v_c) #isobaric
    q_cd = num_mol * (7. / 2.) * gas_constant * (t_d - t_c) 
    ΔE_cd = q_cd - w_cd

    w_da = 0 #isochoric
    q_da = num_mol * (5. / 2.) * gas_constant * (t_a - t_d)
    ΔE_da = q_da - w_da

    print("w_ab =", w_ab, " Joules")
    print("q_ab =", q_ab, " Joules")
    print("ΔE_ab =", ΔE_ab, " Joules")

    print("w_bc =", w_bc, " Joules")
    print("q_bc =", q_bc, " Joules")
    print("ΔE_bc =", ΔE_bc, " Joules")

    print("w_cd =", w_cd, " Joules")
    print("q_cd =", q_cd, " Joules")
    print("ΔE_cd =", ΔE_cd, " Joules")

    print("w_da =", w_da, " Joules")
    print("q_da =", q_da, " Joules")
    print("ΔE_da =", ΔE_da, " Joules")

    #*******
    print ("Part (d")
    #*******

    ΔE_net = ΔE_ab + ΔE_bc + ΔE_cd + ΔE_da
    q_net = q_ab + q_bc + q_cd + q_da
    w_net = w_ab + w_bc + w_cd + w_da

    print("ΔE_net =", ΔE_net, "Joules")
    print("q_net - w_net =", q_net - w_net, "Joules")

    #*******
    print ("Part (e")
    #*******

    ΔS_ab = num_mol * gas_constant * math.log (v_b / v_a)
    ΔS_bc = 0 #adiabatic
    ΔS_cd = num_mol * (7. / 2.) * gas_constant * math.log (t_d / t_c)
    ΔS_da = num_mol * (5. / 2.) * gas_constant * math.log (t_a / t_d)

    ΔS_net = ΔS_ab + ΔS_bc + ΔS_cd + ΔS_da

    print("ΔS_ab =", ΔS_ab, "Joules / Kelvin")
    print("ΔS_bc =", ΔS_bc, "Joules / Kelvin")
    print("ΔS_cd =", ΔS_cd, "Joules / Kelvin")
    print("ΔS_da =", ΔS_da, "Joules / Kelvin")
    print ("ΔS_net = ΔS_ab + ΔS_bc + ΔS_cd + ΔS_da =", ΔS_net, "Joules / Kelvin")

    #*******
    print ("Part (e")
    #*******

    e = w_net / (q_da + q_ab)

    e_c = 1 - (t_d)/ (t_a)

    print ("Efficiency of process: ", e)
    print ("Ratio to that of Carnot Engine: ", e / e_c)


def main() :

     exam2_num3()


    ##call the function you wish to run
    ##change each numbers manually 
    
    

