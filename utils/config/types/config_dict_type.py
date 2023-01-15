from typing import TypedDict


class BanList(TypedDict):
    channel_id: int


class Colors(TypedDict):
    success: int
    error: int
    primary: int | None
    secondary: int | None


class Crisis(TypedDict):
    ignored_categories: list[int]
    ignored_roles: list[int]
    ticket_channels: list[int]
    everyone_role_id: int


class Files(TypedDict):
    allowed_category: int


class GuildInfo(TypedDict):
    member_role_id: int
    guild_uuid: str
    bridge_uuid: str
    member_count_channel_id: int


class GTatsu(TypedDict):
    bridge_bot_ids: list[int]
    bridge_channel_ids: list[int]
    top_active_role_id: int


class HelperAcademy(TypedDict):
    ticket_commands_channel_id: int


class Misc(TypedDict):
    allowed_role_id: int


class Moderation(TypedDict):
    action_log_channel_id: int


class Rep(TypedDict):
    rep_log_channel_id: int


class WeightRoleInfo(TypedDict):
    role_id: int
    weight_req: int
    name: str
    previous: list[int]


class Stats(TypedDict):
    weight_banned_role_id: int
    default_weight_role_id: int
    weight_roles: dict[str, WeightRoleInfo]


class Suggestions(TypedDict):
    suggestions_channel_id: int


class ActivatedTasks(TypedDict):
    update_member_count: bool
    backup_db: bool
    booster_log: bool


class Tasks(TypedDict):
    activated: ActivatedTasks
    total_members_channel_id: int
    booster_role_id: int
    booster_log_channel_id: int


class Qotd(TypedDict):
    qotd_channel_id: int
    qotd_role_id: int


class Verify(TypedDict):
    member_role_id: int
    guild_member_roles: list[int]
    verified_role_id: int


class Config(TypedDict, total=False):
    logo_url: str | None
    server_id: int

    jr_mod_role_id: int
    mod_role_id: int
    admin_role_id: int
    jr_admin_role_id: int
    co_owner_role_id: int
    owner_role_id: int

    mod_chat_channel_id: int
    admin_chat_channel_id: int
    bot_log_channel_id: int

    guilds: dict[str, GuildInfo]
    colors: Colors
    modules: dict[str, bool]
    banlist: BanList
    crisis: Crisis
    files: Files
    gtatsu: GTatsu
    helper_academy: HelperAcademy
    misc: Misc
    moderation: Moderation
    rep: Rep
    stats: Stats
    suggestions: Suggestions
    tasks: Tasks
    qotd: Qotd
    verify: Verify
