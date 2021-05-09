import psycopg2

from typing import List
from psycopg2.extras import execute_batch

from Models.Centro_de_custo import Centro_de_custo
from Models.Departamentos import Departamentos
from Models.Usuarios import Usuarios
from Models.Viagens import Viagens


def PostgreSql_Con(database):
    try:
        connection = psycopg2.connect(host='postgres-dev.clbrkb7i94we.us-east-1.rds.amazonaws.com',
                                      database=database,
                                      user='strroot',
                                      password='iri53mTzA5cnfb9')

    except (Exception, psycopg2.Error) as error:
        if connection:
            print("Failed to insert record into mobile table", error)

    return connection


# oi

def Select(connection, query):
    try:
        cursor = connection.cursor()
        postgres_select = query
        cursor.execute(postgres_select)
        result = cursor.fetchall()
        connection.commit()
        return result
    except (Exception, psycopg2.Error) as error:
        if (connection):
            print("Failed to insert record into mobile table", error)
        else:
            raise error
    finally:
        if (connection):
            cursor.close()
            connection.close()


def InsertUsuarios(connection, Usuarios):
    with connection.cursor() as cursor:
        sql = """ 
                INSERT INTO dm_user
                    (
                    "user_id" ,
                    "user_name" ,
                    "login" ,
                    "phone" ,
                    "email" ,
                    "position" ,
                    "company_id" ,
                    "last_Access"  ,
                    "facebookId" ,
                    "createdAt"
                    ) VALUES 
                    """

        values = "(" + ",".join(["%s" for _ in Company_users[0].as_list()]) + ")"

        sql = sql + values + " ON CONFLICT DO NOTHING"

        try:
            inserts = [tuple(sp.as_list()) for sp in Company_users]
            execute_batch(cursor, sql, inserts, 50000)
            connection.commit()
            print("All Users added")
        except Exception as e:
            print("Error happened", e)
        cursor.close()
        connection.close()


def InsertProperty(connection, objeto):
    with connection.cursor() as cursor:
        sql = """
            INSERT INTO dm_farm (
                farm_id,
                company_id, 
                farm_name, 
                city, 
                state,
                country,
                timezone
            ) VALUES """

        values = "(" + ",".join(["%s" for _ in objeto[0].as_list()]) + ")"

        sql = sql + values + " ON CONFLICT DO NOTHING"

        try:
            inserts = [tuple(ob.as_list()) for ob in objeto]
            execute_batch(cursor, sql, inserts, 50000)
            connection.commit()
            print("All Property added")
        except Exception as e:
            print("Error happened", e)
        cursor.close()
        connection.close()


def InsertProduct(connection, objetos):
    with connection.cursor() as cursor:
        sql = """
            INSERT INTO dm_product (
                product_id,
                technical_name,
                action_mode,
                provider,
                unity,
                category
            ) VALUES """

        values = "(" + ",".join(["%s" for _ in objetos[0].as_list()]) + ")"

        sql = sql + values + " ON CONFLICT DO NOTHING"

        try:
            inserts = [tuple(ob.as_list()) for ob in objetos]
            execute_batch(cursor, sql, inserts, 50000)
            connection.commit()
            print("All Companies added")
        except Exception as e:
            print("Error happened", e)
        cursor.close()
        connection.close()


def InsertCompany(connection, objetos):
    with connection.cursor() as cursor:
        sql = """
            INSERT INTO dm_company (
                "address", 
                "city", 
                "country", 
                "currency", 
                "email", 
                "company_id", 
                "name", 
                "phone1", 
                "phone2",
                "purchasepotential",
                "state", 
                "zipcode"
            ) VALUES """

        values = "(" + ",".join(["%s" for _ in objetos[0].as_list()]) + ")"

        sql = sql + values + " ON CONFLICT DO NOTHING"

        try:
            inserts = [tuple(ob.as_list()) for ob in objetos]
            execute_batch(cursor, sql, inserts, 50000)
            connection.commit()
            print("All Companies added")
        except Exception as e:
            print("Error happened", e)
        cursor.close()
        connection.close()


def InsertSeasonProperty(connection, objeto):
    with connection.cursor() as cursor:
        sql = """ 
                INSERT INTO dm_season_property (
                    "season_property_id", 
                    "propertyid",
                    "seasonid", 
                    "totalareas", 
                    "totalareasinseason", 
                    "totalhectares",
                    "totalhectaresinseason") 
                    VALUES 
                    """

        values = "(" + ",".join(["%s" for _ in objeto[0].as_list()]) + ")"

        sql = sql + values + " ON CONFLICT DO NOTHING"

        try:
            inserts = [tuple(sp.as_list()) for sp in objeto]
            execute_batch(cursor, sql, inserts, 50000)
            connection.commit()
            print("All Season Properties added")
        except Exception as e:
            print("Error happened", e)
        cursor.close()
        connection.close()


def InsertCollect(connection, objeto):
    with connection.cursor() as cursor:
        sql = """ 
                INSERT INTO ft_collect (collect_id, 
                                        area_id,
                                        latitude, 
                                        longitude,
                                        scouter_id, 
                                        characteristic_id,
                                        measurements_id,
                                        value,
                                        start_date,
                                        end_date,
                                        start_time,
                                        end_time) 
                    VALUES 
                    """

        values = "(" + ",".join(["%s" for _ in objeto[0].as_list()]) + ")"

        sql = sql + values + " ON CONFLICT DO NOTHING"

        try:
            inserts = [tuple(sp.as_list()) for sp in objeto]
            execute_batch(cursor, sql, inserts, 50000)
            connection.commit()
            print("All Collect Added")
        except Exception as e:
            print("Error happened", e)
        cursor.close()
        connection.close()


def InsertSeason(connection, objeto):
    with connection.cursor() as cursor:
        sql = """ 
                INSERT INTO dm_season
                     ("id",
                      "actualproductivity",
                      "areatotalinhectares",
                      "companyid", 
                      "cropid", 
                      "endsat", 
                      "name", 
                      "productivityforecast",
                      "productivitylastseason", 
                      "seasonproperties", 
                      "startsat",
                      "deleted")
                    VALUES 
                    """

        values = "(" + ",".join(["%s" for _ in objeto[0].as_list()]) + ")"
        sql = sql + values + " ON CONFLICT DO NOTHING"

        try:
            inserts = [tuple(sp.as_list()) for sp in objeto]
            execute_batch(cursor, sql, inserts, 50000)
            connection.commit()
            print("All Seasons added")
        except Exception as e:
            print("Error happened", e)
        cursor.close()
        connection.close()


def InsertCrop(connection, crop):
    with connection.cursor() as cursor:
        sql = """ 
                INSERT INTO dm_crop
                    (
                    "crop_id" ,
                    "crop_name" ,
                    "productivityUnit" ,
                    "cropType" ,
                    "companyId" ,
                    "varietyProductsId" ,
                    "defaultVarietyId"  ,
                    "wkSlug" ,
                    "phase_name",
                    "phase_description",
                    "phase_cropid",
                    "phase_daysafteremercydefault",
                    "phase_id"

                    ) VALUES 
                    """

        values = "(" + ",".join(["%s" for _ in crop[0].as_list()]) + ")"

        sql = sql + values + " ON CONFLICT DO NOTHING"
        # print(sql)

        try:
            inserts = [tuple(sp.as_list()) for sp in crop]
            # print(inserts)
            execute_batch(cursor, sql, inserts, 50000)
            connection.commit()
            print("All Crops added")
        except Exception as e:
            print("Error happened", e)
        cursor.close()
        connection.close()


def InsertArea(connection, objeto):
    with connection.cursor() as cursor:
        sql = """ 
                INSERT INTO dm_area (coordinates,area_size,farm_id,area_id, area_name, region_id, creation_date, deletion_date)  VALUES 
                    """

        values = "(" + ",".join(["%s" for _ in objeto[0].as_list()]) + ")"

        sql = sql + values + " ON CONFLICT DO NOTHING"

        try:
            inserts = [tuple(sp.as_list()) for sp in objeto]
            execute_batch(cursor, sql, inserts, 50000)
            connection.commit()
            print("All Areas added")
        except Exception as e:
            print("Error happened", e)
        cursor.close()
        connection.close()


def InsertSeasonArea(connection, Season_area):
    with connection.cursor() as cursor:
        sql = """ 
                INSERT INTO dm_season_area
                    (
                    id,
                    areaId,
                    seasonPropertyId,
                    seasonId,
                    cropId,
                    varieties,
                    varietyName,
                    plantingDate,
                    emergencyDate,
                    areaInHectares,
                    methodologyId,
                    lastModified,
                    startsAt,
                    endsAt,
                    deleted
                    ) VALUES 
                    """

        values = "(" + ",".join(["%s" for _ in Season_area[0].as_list()]) + ")"

        sql = sql + values + " ON CONFLICT DO NOTHING"

        try:
            inserts = [tuple(sp.as_list()) for sp in Season_area]
            execute_batch(cursor, sql, inserts, 50000)
            connection.commit()
            print("All Season areas added")
        except Exception as e:
            print("Error happened", e)
        cursor.close()
        connection.close()


def InsertPhenological(connection, Phenology):
    if not len(Phenology):
        return

    with connection.cursor() as cursor:
        sql = """ 
                INSERT INTO ft_phenological_stage
                    (
                    id,
                    area_id,
                    start_date,
                    end_date,
                    phenological_stage
                    ) VALUES 
                    """

        values = "(" + ",".join(["%s" for _ in Phenology[0].as_list()]) + ")"

        sql = sql + values + " ON CONFLICT DO NOTHING"
        # print(sql)

        try:
            inserts = [tuple(sp.as_list()) for sp in Phenology]
            # print(inserts)
            execute_batch(cursor, sql, inserts, 50000)
            connection.commit()
            print("All Phenological stages added")
        except Exception as e:
            print("Error happened", e)
        cursor.close()
        connection.close()


def InsertEventsCheck(connection, EventsCheck):
    if not len(EventsCheck):
        return

    with connection.cursor() as cursor:
        sql = """ 
                INSERT INTO ft_events_check
                    (
                    id,
                    area_id,
                    season_id,
                    farm_id,
                    start_date,
                    end_date,
                    monitoring,
                    annotation,
                    phenology,
                    application
                    ) VALUES 
                    """

        values = "(" + ",".join(["%s" for _ in EventsCheck[0].as_list()]) + ")"

        sql = sql + values + " ON CONFLICT DO NOTHING"

        try:
            inserts = [tuple(sp.as_list()) for sp in EventsCheck]
            execute_batch(cursor, sql, inserts, 50000)
            connection.commit()
            print("All Events Check added")
        except Exception as e:
            print("Error happened", e)
        cursor.close()
        connection.close()


def InsertMonitorings(connection, Monitorings):
    with connection.cursor() as cursor:
        sql = """ 
                INSERT INTO ft_collections_issue
                    (
                    id,
                    area_id,
                    indicator_name,
                    indicator_id,
                    indicator_value,
                    collection_start_date,
                    collection_end_date,
                    phenomenon_id,
                    phenomenon_name,
                    indicator_level,
                    unit,
                    season_id
                    ) VALUES 
                    """

        values = "(" + ",".join(["%s" for _ in Monitorings[0].as_list()]) + ")"

        sql = sql + values + " ON CONFLICT DO NOTHING"
        # print(sql)

        try:
            inserts = [tuple(sp.as_list()) for sp in Monitorings]
            # print(inserts)
            execute_batch(cursor, sql, inserts, 50000)
            connection.commit()
            print("All Monitorings added")
        except Exception as e:
            print("Error happened", e)
        cursor.close()
        connection.close()


def InsertIndicators(connection, Indicators):
    with connection.cursor() as cursor:
        sql = """ 
                INSERT INTO dm_indicator
                    (
                    company_id,
                    created_at,
                    modified_at,
                    phenomenon_id,
                    characteristic_id,
                    indicator_expression,
                    indicator_unit,
                    indicator_id,
                    control_threshold,
                    damage_threshold,
                    indicator_name
                    ) VALUES 
                    """

        values = "(" + ",".join(["%s" for _ in Indicators[0].as_list()]) + ")"

        sql = sql + values + " ON CONFLICT DO NOTHING"
        # print(sql)

        try:
            inserts = [tuple(sp.as_list()) for sp in Indicators]
            # print(inserts)
            execute_batch(cursor, sql, inserts, 50000)
            connection.commit()
            print("All Indicators added")
        except Exception as e:
            print("Error happened", e)
        cursor.close()
        connection.close()


def InsertSprays(connection, Spray):
    with connection.cursor() as cursor:
        sql = """ 
                INSERT INTO ft_application
                    (
                    uuid,
                    id_application,
                    area_id,
                    scouter_id,
                    scouter_name,
                    created_at,
                    start_date,
                    end_date,
                    product_id,
                    dose,
                    product_unit,
                    total,
                    sprayed_area,
                    flow_rate,
                    flow_rate_unit,
                    total_amount,
                    total_amount_unit,
                    machine,
                    angle,
                    spray_mode,
                    wind_speed,
                    wind_direction,
                    soil_humidity,
                    deleted

                    ) VALUES 
                    """

        values = "(" + ",".join(["%s" for _ in Spray[0].as_list()]) + ")"
        sql = sql + values + " ON CONFLICT DO NOTHING"

        try:
            inserts = [tuple(sp.as_list()) for sp in Spray]
            execute_batch(cursor, sql, inserts, 50000)
            connection.commit()
            print("All Spray added")
        except Exception as e:
            print("Error happened", e)
        cursor.close()
        connection.close()


def InsertMethodologies(connection, methodologies: List[Methodology]):
    with connection.cursor() as cursor:
        sql = """ 
            INSERT INTO dm_methodology (
                methodology_id,
                company_id,
                crop_id,
                indicator_id,
                control_threshold,
                damage_threshold
            ) VALUES """

        values = "(" + ",".join(["%s" for _ in methodologies[0].as_list()]) + ")"

        sql = sql + values + " ON CONFLICT DO NOTHING"

        try:
            inserts = [tuple(m.as_list()) for m in methodologies]
            execute_batch(cursor, sql, inserts, 50000)
            connection.commit()
            print("All Methodologies added")
        except Exception as e:
            print("Error happened ", e)
        cursor.close()
        connection.close()


def InsertCharacteristics(connection, characteristics: List[Characteristic]):
    with connection.cursor() as cursor:
        sql = """ 
            INSERT INTO dm_characteristic (
                characteristic_id,
                characteristic_name,
                phenomenon_id
            ) VALUES """

        values = "(" + ",".join(["%s" for _ in characteristics[0].as_list()]) + ")"

        sql = sql + values + " ON CONFLICT DO NOTHING"

        try:
            inserts = [tuple(c.as_list()) for c in characteristics]
            execute_batch(cursor, sql, inserts, 50000)
            connection.commit()
            print("All Characteristics added")
        except Exception as e:
            print("Error happened ", e)
        cursor.close()
        connection.close()


def InsertPhenomenons(connection, phenomenons: List[Phenomenon]):
    with connection.cursor() as cursor:
        sql = """ 
            INSERT INTO dm_phenomenon (
                phenomenon_id,
                phenomenon_name,
                category_id,
                category_name,
                scientific_name
            ) VALUES """

        values = "(" + ",".join(["%s" for _ in phenomenons[0].as_list()]) + ")"

        sql = sql + values + " ON CONFLICT DO NOTHING"

        try:
            inserts = [tuple(p.as_list()) for p in phenomenons]
            execute_batch(cursor, sql, inserts, 50000)
            connection.commit()
            print("All Phenomenons added")
        except Exception as e:
            print("Error happened ", e)
        cursor.close()
        connection.close()


def UpdateJobs(connection, tablename):
    try:
        cursor = connection.cursor()
        postgres_insert_query = "update jobs set id_processamento = true where name = '" + tablename + "'"

        cursor.execute(postgres_insert_query)
        connection.commit()
    except (Exception, psycopg2.Error) as error:
        if connection:
            print("Failed to insert record into mobile table", error)
        else:
            raise error
    finally:
        if connection:
            cursor.close()
            connection.close()


def UpdateFarm(connection, query):
    try:
        connection = connection
        cursor = connection.cursor()
        postgres_insert_query = query

        cursor.execute(postgres_insert_query)
        connection.commit()
    except (Exception, psycopg2.Error) as error:
        if connection:
            print("Failed to insert record into mobile table", error)
        else:
            raise error
    finally:
        if connection:
            cursor.close()
            connection.close()


def UpdateGeography(connection, query):
    try:
        connection = connection
        cursor = connection.cursor()
        postgres_insert_query = query

        cursor.execute(postgres_insert_query)
        connection.commit()
    except (Exception, psycopg2.Error) as error:
        if connection:
            print("Failed to insert record into mobile table", error)
        else:
            raise error
    finally:
        if connection:
            cursor.close()
            connection.close()


def insert_time(connection, elapsed_time, type, urlapi, log, time, company_id, season_id):
    with connection.cursor() as cursor:
        sql = """ 
            INSERT INTO api_time (
                elapsed_insert_time,
                type,
                urlapi,
                log,
                time,
                company_id,
                season_id
            ) VALUES (
                 {}, '{}', '{}', '{}', '{}', '{}', '{}'
            )""".format(elapsed_time, type, urlapi, log, time, company_id, season_id)
        try:
            cursor.execute(sql)
            connection.commit()
        except Exception as e:
            print("Error happened ", e)


def InsertDeletedProperty(connection, objeto):
    with connection.cursor() as cursor:
        sql = """
            INSERT INTO dm_deleted_farm (
                farm_id,
                company_id, 
                farm_name, 
                city, 
                state
            ) VALUES """

        values = "(" + ",".join(["%s" for _ in objeto[0].as_list()]) + ")"

        sql = sql + values + " ON CONFLICT DO NOTHING"

        try:
            inserts = [tuple(ob.as_list()) for ob in objeto]
            execute_batch(cursor, sql, inserts, 50000)
            connection.commit()
            print("All Property added")
        except Exception as e:
            print("Error happened", e)
        cursor.close()
        connection.close()


def InsertRegion(connection, regions: List[Region]):
    with connection.cursor() as cursor:
        sql = """
            INSERT INTO dm_region (
                region_id,
                region_name, 
                parent_id, 
                property_id, 
                created_at,
                last_modified,
                deleted_at
            ) VALUES """

        values = "(" + ",".join(["%s" for _ in regions[0].as_list()]) + ")"

        sql = sql + values + " ON CONFLICT DO NOTHING"

        try:
            inserts = [tuple(ob.as_list()) for ob in regions]
            execute_batch(cursor, sql, inserts, 50000)
            connection.commit()
            print("All Regions added")
        except Exception as e:
            print("Error happened", e)
        cursor.close()
        connection.close()
