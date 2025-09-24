# Import & Loading Libraries
import streamlit as st
import pandas as pd
import pickle

# Load model

import joblib
model = joblib.load("bestmodelwithtuning.pkl")

def run():
    st.title("🚗 Prediksi Harga Pasar Mobil Bekas")

    with st.form("Car Market Price Prediction Form"):
        st.markdown("<h3 style='text-align: center;'>📋 Formulir Data Mobil</h3>", unsafe_allow_html=True)

        # Input fitur mobil
        year = st.number_input("Tahun Produksi", min_value=1980, max_value=2025, value=2015, help="Masukkan tahun produksi mobil (1980-2025).")
        make = st.selectbox("Merk Mobil", ['Hyundai', 'Jeep', 'Ford', 'Chevrolet', 'Honda', 'Infiniti',
                                           'Nissan', 'Lexus', 'Dodge', 'Volvo', 'Toyota', 'GMC',
                                           'Mercedes-Benz', 'Ram', 'BMW', 'Kia', 'Cadillac', 'Lincoln',
                                           'Chrysler', 'Volkswagen', 'Mercury', 'Subaru', 'Buick', 'Pontiac',
                                           'Audi', 'Porsche', 'Mitsubishi', 'Land Rover', 'MINI', 'Mazda',
                                           'Jaguar', 'Saturn', 'Scion', 'Acura', 'FIAT', 'HUMMER', 'Saab',
                                           'Suzuki', 'Bentley', 'smart', 'Isuzu', 'Oldsmobile', 'Tesla',
                                           'Fisker'])

        model_name = st.selectbox("Model Mobil", ['Elantra', 'Patriot', 'Edge', 'Impala', 'Fusion', 'Crosstour','Malibu', 'Q50', 'Altima', 'Sentra', 'GS 350', 'Dart', 'C70','Odyssey', 'Challenger', 'Camry', 'Journey', 'Terrain', 'Altima Hybrid', 'Focus', 'C-Class', 'Escape', 'Maxima', 'Liberty','3500', '3 Series', 'Soul', 'Cruze', 'S-Class', 'X5','Explorer Sport Trac', 'Spectra', 'Escalade', 'MKT', 'Fiesta','Rio', 'Town and Country', 'Wrangler', 'Equinox', 'Santa Fe','Passat', 'Mustang', 'Compass', 'Transit Connect', 'Acadia', 'Silverado 1500', 'XTS', 'Windstar', 'HHR', 'Mountaineer', 'TrailBlazer', 'CTS', 'Impreza', 'LS 460', 'Civic', 'Outback','G Sedan', 'Explorer', 'F-150', 'LaCrosse', 'Silverado 2500HD','Matrix', 'Suburban', 'Azera', 'Grand Cherokee', 'Highlander', 'G6', 'G35', 'F-250 Super Duty', 'Q7', 'Cayenne', 'Optima','Lancer', 'Envoy XL', 'M', 'GLK-Class', 'Range Rover Sport','Taurus', 'Sorento', 'Corolla', 'DeVille', 'Ram Pickup 1500','RX 350', 'E-Series Van', 'CC', 'EX', 'Cooper Paceman', 'Tucson','PT Cruiser', 'ES 330', 'Cooper', 'Genesis', 'MX-5 Miata', 'Pilot','Pathfinder', 'Cooper Countryman', 'S80', 'RAV4', 'Charger','Rogue', '200', 'Venture', 'CX-9', 'Avalanche', 'Jetta','XJ-Series', 'Yaris', 'Grand Caravan', 'cl55', 'Sonata', 'Versa', 'Accord', 'Tahoe', 'Ram Pickup 2500', 'GTI', 'CR-V', 'Aura', 'G Coupe', 'E-Class', 'Avenger', 'VUE', 'Expedition', 'Z4', '300', '1500', 'G8', 'xB', 'Frontier', 'A6', 'SRX', 'Sienna', 'TL', 'Verano', 'RX 300', 'Galant', 'Mazda3', 'Five Hundred',       'Grand Prix', 'tC', 'ES 350', 'Torrent', '5 Series', 'Murano', 'Yukon', 'Element', 'Elantra Coupe', 'CX-5', 'Savana Cargo', 'Impala Limited', 'C/V Cargo Van', 'Legacy', 'Prius', 'Forester', 'F-450 Super Duty', 'Cube', 'Flex', 'Monte Carlo', 'Touareg',       'Forte', '500L', 'Sebring', 'CLK-Class', 'Fit', 'Sportage', 'Camaro', 'ILX', 'Econoline Wagon', 'Blazer', 'Golf', 'Grand Marquis', 'Equus', 'Cherokee', 'Tacoma', 'Express Cargo', 'Sonic', 'CLS-Class', 'S-10 Blazer', 'Tahoe Hybrid', 'Caliber',       'A8', 'Accent', 'Titan', 'Mazda5', 'Navigator', 'Tiguan', 'Rogue Select', 'Tundra', 'Captiva Sport', 'Rainier', 'JX', 'MKS','LS 430', 'Ranger', 'G Convertible', 'Silverado 1500 Classic', 'Nitro', 'M-Class', 'A4', 'Cobalt', 'XC60', 'Q5', 'c230wz', 'XJ',   '4Runner', 'Century', 'Econoline Cargo', 'X3', 'Focus ST', 'Armada', '2500', 'Mirage', 'TSX', '370Z', 'Expedition EL','F-350 Super Duty', 'Escalade ESV', 'Ram Pickup 3500','New Beetle', 'Yukon XL', 'E-Series Wagon', 'S4', 'Tiburon', 'ION',       'Leaf', 'X6', 'Sierra 1500', 'gx', 'B9 Tribeca', 'XF', 'RX 330', 'Avalon', 'Uplander', 'Outlander', 'C-Max Hybrid', 'pilot',   'Quest', 'RDX', '7 Series', 'Stratus', 'IS 250', 'Xterra','Genesis Coupe', 'Silverado 3500 Classic', 'S2000', 'FX', 'XC',       'SL-Class', 'A3', 'S70', 'H3', '9-7X', 'lx', 'Versa Note', 'Volt', 'Taurus X', 'S60', 'Mazda6', 'Forenza', 'Cooper Coupe', 'L300',       'Malibu Classic', 'Fusion Hybrid', 'Town Car', 'Silverado 3500HD', 'Dakota', 'Colorado', 'LeSabre', 'Continental Flying Spur', 'H2',       'M37', 'Traverse', 'Veloster', 'fortwo', 'Cadenza', '6 Series', 'Beetle', 'Grand Am', 'GL-Class', 'town', 'QX56', 'S40', 'Mazda2',       'Sequoia', 'X1', 'MDX', 'IS 250 C', 'CTS Wagon', 'Aviator', 'Camry Solara', 'Commander', 'Celica', 'Santa Fe Sport', 'Pacifica', 'Lancer Evolution', 'XC90', 'Venza', 'Sierra 2500HD', 'M35', 'Express', 'Lucerne', 'Neon', 'XK', 'Caravan', 'CL-Class',       'iQ', 'Juke', 'Outlander Sport', 'pacifica', 'Enclave', 'Durango', '1 Series', 'Millenia', 'Seville', 'xD', 'Catera', 'MKX', 'A7',       'IS F', 'NV', 'Mariner', 'Q3', 'GS 300', 'SC 430', 'Veracruz', 'LS', 'Outlook', 'forester', 'Montego', 'Prius c', 'DTS', 'Envoy',       'Spark', 'hhr', 'Cooper Clubman', 'cx-7', 'Land Cruiser', 'Escalade EXT', 'M5', 'RX 450h', 'A5', 'Rendezvous', 'Routan',       'Panamera', 'Sedona', 'MKZ', 'S-Type', 'Accord Crosstour', 'Rodeo','Aveo', 'Bravada', 'Sierra 3500HD', 'jetta', 'Eclipse', 'QX',       'Range Rover', 'HS 250h', 'Escape Hybrid', 'Camry Hybrid', 'GS 450h', 'SSR', 'Tribute', 'Transit Van', 'Cavalier', 'Magnum',       'Jetta GLI', 'Vibe', 'Highlander Hybrid', 'LS 400', 'TrailBlazer EXT', 'ECHO', '5 Series Gran Turismo', 'CT 200h',       'M3', 'Protege', 'V60', 'XL7', 'Ridgeline', 'S5', 'MPV', 'i8', 'LX 470', '4 Series', 'SX4', 'X-Type', 'Cabrio',   'Range Rover Evoque', 'GT-R', 'QX80', 'C/V Tradesman', 'Prius Plug-in', 'Touareg 2', 'FR-S', 'Quattroporte', 'Golf R',       'Rabbit', 'FJ Cruiser', 'Montana', 'LR4', 'thunderbird', 'grand','Aspen', 'CTS Coupe', 'Sky', 'Escort', 'Milan', 'malibu', 'Alero',       'Sonata Hybrid', 'rl', 'corvette', 'Freestyle', 'STS', 'Encore', 'Freestar', 'Solstice', 'GX 460', 'Sunfire', 'Sprinter Cargo',       'ES 300', 'RS 5', '500', 'Silverado 1500HD', 'Shelby GT500', 'QX4','Impreza WRX', 'F-150 Heritage', 'Yukon Hybrid', 'MR2 Spyder', 'CLA-Class', 'Regal', 'CX-7', 'Sable', 'Zephyr', 'CR-Z', 'Borrego','i-MiEV', 'Explorer Sport', 'Envoy XUV', 'Civic del Sol', 'LHS',       'Continental GT', 'Insight', 'MKC', 'Montero Sport', 'f150', 'I30','Jetta SportWagen', 'RX 400h', '911', 'G-Class', 'ATS',       'Discovery Series II', 'Aurora', 'mazda3', 'Beetle Convertible', 'R-Class', 'Endeavor', 'allroad', 'Model S', 'IS 300',       'Avalon Hybrid', 'RSX', 'Thunderbird', 'sts', '9-3','Elantra Touring', 'Boxster', 'Lumina', '6 Series Gran Coupe',       'Baja', '626', '300M', 'CTS-V Coupe', 'mazda5', 'IS 350', 'EX35','C-Max Energi', 'Corvette', 'Tracker', 'Eos', 'GS 430', 'uplander',       'Entourage', 'ES 300h', 'Malibu Maxx', 'Karma', 'QX70', 'Verona','350Z', 'TSX Sport Wagon', 'Cayman', 'Classic', 'Q60 Coupe', 'rx8',       'e150', 'M6 Gran Coupe', 'G5', 'Corvette Stingray', 'S6','ridgelin', 'Bonneville', 'CTS-V', 'f250', 'Park Avenue', 'galant',       'M6', 'Crossfire', 'S-Series', 'range', 'Trooper', 'Diamante','Amanti', 'Passport', 'QX60', 'XC70', 'Silverado 2500HD Classic', 'Malibu Hybrid', 'XV Crosstrek', 'FX35', 'explorer','Silverado 3500', 'Elantra GT', '350z', 'Integra', 'GS 400', 'BRZ',       'Kizashi', '9-5', 'TT', 'XK-Series', 'SLK-Class', 'Continental GTC', 'srx', 'XL-7', 'Relay', '9-2X', 'Mazdaspeed3', 'compass', 'Mark LT', 'Lancer Sportback', 'LR2', 'Astro Cargo', 'I35', 's10', 'e350', 'Intrepid', 'Excursion','3 Series Gran Turismo', 'gr', 'Ghibli', 'Z3', 'Cirrus', 'Windstar Cargo', 'Mazdaspeed Mazda3', 'Silhouette', 'Prizm', 'FX45', 'WRX', 'Pickup', 'Viper', 'G37', 'S-10', 'Monterey', 'G3',       'Astra', 'Tribeca', 'L-Series', 'g55', 'Rondo', 'stratus', 'VUE Hybrid', 'mazda6', 'V70', 'Grand Vitara', 'NV Cargo',      'Intrigue', 'sonoma', 'Firebird', 'Navigator L', 'voyager','RC 350', 'XG350', 'g1500', 'magnum'])

        trim = st.selectbox("Trim Mobil", ['GLS', 'Limited', 'LS', 'SE', 'EX', 'Base', 'LTZ', 'Premium', 'Sport','Touring', 'XLE', 'SLT', 'Denali', 'Laramie', 'SXT', 'LT', 'EX-L', 'LX', 'Platinum', 'Titanium', 'Eco', 'Classic', 'Luxury', 'Rubicon', 'Unlimited','GT', 'SV', 'SR', 'SL', 'SS', 'Z71', 'R/T', 'SLE', 'AWD', 'V6', 'V8'])
        body = st.selectbox("Jenis Body", ['Sedan', 'SUV', 'Hatchback', 'Coupe', 'Convertible', 'Minivan',
                                           'Van', 'Truck', 'Wagon', 'Crew Cab', 'Extended Cab', 'Regular Cab',
                                           'SuperCab', 'SuperCrew', 'Double Cab', 'Mega Cab'])

        transmission = st.selectbox("Transmisi", ['Automatic', 'Manual'])
        branch = st.selectbox("Lokasi Cabang", ['JAKARTA', 'SURABAYA', 'MEDAN', 'BALIKPAPAN'])
        condition = st.slider("Skor Kondisi Mobil (0–50)", min_value=0.0, max_value=50.0, step=0.5, value=45.0, help="Skor kondisi mobil dari 0 (terburuk) hingga 50 (terbaik).")
        odometer = st.number_input("Jarak Tempuh (km)", min_value=0.0, max_value=500000.0, value=30000.0)
        color = st.selectbox("Warna Eksterior", ['Black', 'White', 'Gray', 'Brown', 'Gold', 'Silver', 'Red',
                                                 'Blue', 'Burgundy', 'Turquoise', 'Beige', 'Green', 'Orange',
                                                 'Purple', 'Off-White', 'Yellow', 'Charcoal'])

        interior = st.selectbox("Warna Interior", ['Beige', 'Tan', 'Black', 'Gray', 'Brown', 'Purple', 'Blue',
                                                   'Off-White', 'Red', 'Silver', 'Burgundy', 'White', 'Green',
                                                   'Gold', 'Orange', 'Yellow'])

        submit = st.form_submit_button("Prediksi Harga Pasar")

        if submit:
            input_data = pd.DataFrame({
                'year': [year],
                'make': [make],
                'model': [model_name],
                'trim': [trim],
                'body': [body],
                'transmission': [transmission],
                'branch': [branch],
                'condition': [condition],
                'odometer': [odometer],
                'color': [color],
                'interior': [interior]
            })

            try:
                pred_price = model.predict(input_data)[0]
                st.success(f"💰 Prediksi harga pasar mobil: {int(pred_price):,}")
            except Exception as e:
                st.error(f"❌ Gagal melakukan prediksi: {e}")