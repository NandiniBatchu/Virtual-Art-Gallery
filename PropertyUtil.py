class PropertyUtil:
    @staticmethod
    def getPropertyString(property_file_path=r"C:\Users\Nandini\Downloads\VirtualArtGallery (1)"):
        try:
            with open(property_file_path, 'r') as file:
                properties = {}
                for line in file:
                    if '=' in line:
                        key, value = line.strip().split('=', 1)  # Split by '=' only on the first occurrence
                        properties[key.strip()] = value.strip()
                
                # Create the connection string
                connection_string = f"DRIVER={{ODBC Driver 17 for SQL Server}};" \
                                    f"SERVER={properties['server']};" \
                                    f"DATABASE={properties['dbname']};" \
                                    f"Trusted_Connection={properties['trusted_connection']};"
                return connection_string
        except ValueError as ve:
            print('db is missing',ve)
        except Exception as e:
            print(f"Error reading property file: {e}")
            return None
