class Region:

    def __init__(self, woj_id, powiat_id, gmina_id, rgmi_id, name, community_type):
        self.name = name
        self.community_type = community_type
        self.woj_id = woj_id
        self.powiat_id = powiat_id
        self.gmina_id = gmina_id
        self.rgmi_id = rgmi_id

    def get_name(self):
        return self.name

    def get_region_type(self):
        return self.community_type

    def get_powiat_id(self):
        return self.powiat_id

    def get_wojewodztwo_id(self):
        return self.woj_id

    @staticmethod
    def get_list_of_all_locations():
        list_of_all = Wojewodztwo.get_list() + Powiat.get_list() + MiastoNaPrawachPowiatu.get_list() + GminaMiejska.get_list() + \
            GminaWiejska.get_list() + GminaMiejskoWiejska.get_list() + ObszarWiejski.get_list() + \
            Miasto.get_list() + Delegatura.get_list()
        return list_of_all


class Wojewodztwo(Region):
    _wojewodztwa_list = []

    def __init__(self, woj_id, powiat_id, gmina_id, rgmi_id, name, community_type):
        super().__init__(woj_id, powiat_id, gmina_id, rgmi_id, name, community_type)
        self.powiaty = []
        self._wojewodztwa_list.append(self)

    @classmethod
    def add_powiat(cls, powiat):
        for wojewodztwo in cls._wojewodztwa_list:
            if wojewodztwo.get_wojewodztwo_id() == powiat.get_wojewodztwo_id():
                wojewodztwo.powiaty.append(powiat)
                return

    @classmethod
    def get_list(cls):
        return cls._wojewodztwa_list


class Powiat(Region):
    _powiaty_list = []

    def __init__(self, woj_id, powiat_id, gmina_id, rgmi_id, name, community_type):
        super().__init__(woj_id, powiat_id, gmina_id, rgmi_id, name, community_type)
        self.communities = []
        if type(self) == Powiat:  # because then MiastoNaPrawachPowiatu add self to _powiaty_list and _miast[...]list
            self._powiaty_list.append(self)

    @classmethod
    def add_community(cls, community):
        for powiat in cls._powiaty_list:
            if powiat.get_powiat_id() == community.get_powiat_id():
                powiat.communities.append(community)
                return

    @classmethod
    def get_list(cls):
        return cls._powiaty_list

    def get_communities_list(self):
        return self.communities

    def __gt__(self, other):
        if other == None:
            return True
        return len(self.communities) > len(other.communities)


class MiastoNaPrawachPowiatu(Powiat):
    _miasta_na_prawach_powiatu_list = []

    def __init__(self, woj_id, powiat_id, gmina_id, rgmi_id, name, community_type):
        super().__init__(woj_id, powiat_id, gmina_id, rgmi_id, name, community_type)
        self._miasta_na_prawach_powiatu_list.append(self)

    @classmethod
    def get_list(cls):
        return cls._miasta_na_prawach_powiatu_list


class GminaMiejska(Region):
    _gminy_miejskie_list = []

    def __init__(self, woj_id, powiat_id, gmina_id, rgmi_id, name, community_type):
        super().__init__(woj_id, powiat_id, gmina_id, rgmi_id, name, community_type)
        self._gminy_miejskie_list.append(self)

    @classmethod
    def get_list(cls):
        return cls._gminy_miejskie_list


class GminaWiejska(Region):
    _gminy_wiejskie_list = []

    def __init__(self, woj_id, powiat_id, gmina_id, rgmi_id, name, community_type):
        super().__init__(woj_id, powiat_id, gmina_id, rgmi_id, name, community_type)
        self._gminy_wiejskie_list.append(self)

    @classmethod
    def get_list(cls):
        return cls._gminy_wiejskie_list


class GminaMiejskoWiejska(Region):
    _gminy_miejsko_wiejskie_list = []

    def __init__(self, woj_id, powiat_id, gmina_id, rgmi_id, name, community_type):
        super().__init__(woj_id, powiat_id, gmina_id, rgmi_id, name, community_type)
        self._gminy_miejsko_wiejskie_list.append(self)

    @classmethod
    def get_list(cls):
        return cls._gminy_miejsko_wiejskie_list


class ObszarWiejski(Region):
    _obszary_wiejskie_list = []

    def __init__(self, woj_id, powiat_id, gmina_id, rgmi_id, name, community_type):
        super().__init__(woj_id, powiat_id, gmina_id, rgmi_id, name, community_type)
        self._obszary_wiejskie_list.append(self)

    @classmethod
    def get_list(cls):
        return cls._obszary_wiejskie_list


class Miasto(Region):
    _miasta_list = []

    def __init__(self, woj_id, powiat_id, gmina_id, rgmi_id, name, community_type):
        super().__init__(woj_id, powiat_id, gmina_id, rgmi_id, name, community_type)
        self._miasta_list.append(self)

    @classmethod
    def get_list(cls):
        return cls._miasta_list


class Delegatura(Region):
    _delegatury_list = []

    def __init__(self, woj_id, powiat_id, gmina_id, rgmi_id, name, community_type):
        super().__init__(woj_id, powiat_id, gmina_id, rgmi_id, name, community_type)
        self._delegatury_list.append(self)

    @classmethod
    def get_list(cls):
        return cls._delegatury_list
