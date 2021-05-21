# coding: utf-8
from sqlalchemy import Column, Date, DateTime, Index, String, Text, text
from sqlalchemy.dialects.mysql import INTEGER, LONGTEXT, TINYINT, VARCHAR, DOUBLE, DECIMAL
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()
metadata = Base.metadata

class AccountsUser(Base):
    __tablename__ = 'accounts_user'

    id = Column(INTEGER(11), primary_key=True, index=True)
    password = Column(VARCHAR(128))
    last_login = Column(DateTime, nullable=False)
    is_superuser = Column(TINYINT(1))
    username = Column(VARCHAR(150))
    first_name = Column(VARCHAR(30))
    last_name = Column(VARCHAR(30))
    email = Column(VARCHAR(254))
    is_staff = Column(TINYINT(1))
    date_joined = Column(DateTime, nullable=False)
    phone = Column(VARCHAR(30))
    is_active = Column(TINYINT(1))
    creator_id = Column(INTEGER(11))
    accept_privacy_policy = Column(DateTime, nullable=False)
    consume_tapeta_2020 = Column(TINYINT(1))



class ProjectsProject(Base):
    __tablename__ = 'projects_project'

    id = Column(INTEGER(11), primary_key=True, index=True)
    name = Column(VARCHAR(140))
    date_creation = Column(DateTime, nullable=False)
    date_modification = Column(DateTime, nullable=False)
    product = Column(VARCHAR(60))
    glass_thickness = Column(VARCHAR(60))
    bars_length = Column(VARCHAR(60))
    drawing = Column(VARCHAR(100))
    remarks = Column(LONGTEXT)
    ral_kind = Column(VARCHAR(60))
    ral = Column(VARCHAR(120))
    is_active = Column(TINYINT(1))
    client_id = Column(INTEGER(11))
    creator_id = Column(INTEGER(11))
    is_special = Column(TINYINT(1))
    remarks_special = Column(LONGTEXT)
    carries_glass = Column(TINYINT(1))
    remarks_internal = Column(LONGTEXT)
    door_cut = Column(TINYINT(1))
    stop_90 = Column(TINYINT(1))
    flush_handle_panel_enlargement = Column(TINYINT(1))
    lock_panel_enlargement = Column(TINYINT(1))
    ral_marine_tratament = Column(TINYINT(1))
    strip_kind = Column(VARCHAR(60))


class ProjectsProjectcomponent(Base):
    __tablename__ = 'projects_projectcomponent'

    id = Column(INTEGER(11), primary_key=True, index=True)
    quantity = Column(DOUBLE)
    is_active = Column(TINYINT(1))
    component_id = Column(INTEGER(11))
    project_id = Column(INTEGER(11))


class ComponentsComponent(Base):
    __tablename__ = 'components_component'

    id = Column(INTEGER(11), primary_key=True, index=True)
    category = Column(VARCHAR(50))
    code = Column(VARCHAR(50), unique=True)
    composition = Column(VARCHAR(50))
    description = Column(LONGTEXT)
    image = Column(VARCHAR(100))
    measure_unit = Column(VARCHAR(50))
    name = Column(VARCHAR(140))
    name_de = Column(VARCHAR(140))
    name_en = Column(VARCHAR(140))
    name_es = Column(VARCHAR(140))
    name_fr = Column(VARCHAR(140))
    name_it = Column(VARCHAR(140))
    name_pl = Column(VARCHAR(140))
    name_pt = Column(VARCHAR(140))
    name_ru = Column(VARCHAR(140))
    position = Column(VARCHAR(50))
    price = Column(DECIMAL(10, 4))
    price_insystem = Column(DECIMAL(10, 4))
    product = Column(VARCHAR(50))
    weight = Column(DECIMAL(10, 4))
    is_active = Column(TINYINT(1))
    name_ko = Column(VARCHAR(140))
    is_reportable = Column(TINYINT(1))
    is_saleable = Column(TINYINT(1))


