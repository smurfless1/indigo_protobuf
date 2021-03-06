# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: proto/indigo.proto
# plugin: python-betterproto
from dataclasses import dataclass
from datetime import datetime
from typing import AsyncGenerator, Optional

import betterproto
import grpclib


@dataclass
class DeviceChange(betterproto.Message):
    name: Optional[str] = betterproto.message_field(1, wraps=betterproto.TYPE_STRING)


@dataclass
class IndigoEvent(betterproto.Message):
    measurement: Optional[str] = betterproto.message_field(
        1, wraps=betterproto.TYPE_STRING
    )
    time: datetime = betterproto.message_field(5)
    tags: "IndigoTags" = betterproto.message_field(3)
    fields: "IndigoFields" = betterproto.message_field(4)


@dataclass
class IndigoFields(betterproto.Message):
    name: Optional[str] = betterproto.message_field(1, wraps=betterproto.TYPE_STRING)
    last_changed: Optional[float] = betterproto.message_field(
        2, wraps=betterproto.TYPE_FLOAT
    )
    last_successful_comm: Optional[float] = betterproto.message_field(
        3, wraps=betterproto.TYPE_FLOAT
    )
    id: Optional[float] = betterproto.message_field(4, wraps=betterproto.TYPE_FLOAT)
    brightness: Optional[float] = betterproto.message_field(
        10, wraps=betterproto.TYPE_FLOAT
    )
    on_state: Optional[bool] = betterproto.message_field(
        11, wraps=betterproto.TYPE_BOOL
    )
    state_on_off_state: Optional[bool] = betterproto.message_field(
        12, wraps=betterproto.TYPE_BOOL
    )
    on_state_num: Optional[float] = betterproto.message_field(
        13, wraps=betterproto.TYPE_FLOAT
    )
    state_humidity_input1: Optional[float] = betterproto.message_field(
        21, wraps=betterproto.TYPE_FLOAT
    )
    cool_setpoint: Optional[float] = betterproto.message_field(
        22, wraps=betterproto.TYPE_FLOAT
    )
    cool_is_on: Optional[bool] = betterproto.message_field(
        23, wraps=betterproto.TYPE_BOOL
    )
    cool_is_on_num: Optional[float] = betterproto.message_field(
        24, wraps=betterproto.TYPE_FLOAT
    )
    heat_setpoint: Optional[float] = betterproto.message_field(
        25, wraps=betterproto.TYPE_FLOAT
    )
    heat_is_on: Optional[bool] = betterproto.message_field(
        26, wraps=betterproto.TYPE_BOOL
    )
    heat_is_on_num: Optional[float] = betterproto.message_field(
        27, wraps=betterproto.TYPE_FLOAT
    )
    state_temperature_input1: Optional[float] = betterproto.message_field(
        29, wraps=betterproto.TYPE_FLOAT
    )


@dataclass
class IndigoTags(betterproto.Message):
    name: Optional[str] = betterproto.message_field(1, wraps=betterproto.TYPE_STRING)
    folder: Optional[str] = betterproto.message_field(2, wraps=betterproto.TYPE_STRING)
    folder_id: Optional[str] = betterproto.message_field(
        3, wraps=betterproto.TYPE_STRING
    )


@dataclass
class HvacFields(betterproto.Message):
    dehumidifier_is_on_num: Optional[float] = betterproto.message_field(
        1, wraps=betterproto.TYPE_FLOAT
    )
    supports_cool_setpoint_num: Optional[float] = betterproto.message_field(
        2, wraps=betterproto.TYPE_FLOAT
    )
    state_hvac_operation_mode_is_off: Optional[bool] = betterproto.message_field(
        3, wraps=betterproto.TYPE_BOOL
    )
    state_hvac_heater_is_on: Optional[bool] = betterproto.message_field(
        4, wraps=betterproto.TYPE_BOOL
    )
    plugin_id: Optional[str] = betterproto.message_field(
        5, wraps=betterproto.TYPE_STRING
    )
    last_successful_comm: Optional[float] = betterproto.message_field(
        6, wraps=betterproto.TYPE_FLOAT
    )
    protocol: Optional[str] = betterproto.message_field(
        7, wraps=betterproto.TYPE_STRING
    )
    state_hvac_fan_is_on: Optional[bool] = betterproto.message_field(
        8, wraps=betterproto.TYPE_BOOL
    )
    error_state: Optional[str] = betterproto.message_field(
        9, wraps=betterproto.TYPE_STRING
    )
    state_hvac_dehumidifier_is_on_num: Optional[float] = betterproto.message_field(
        10, wraps=betterproto.TYPE_FLOAT
    )
    state_humidity_inputs_all: Optional[str] = betterproto.message_field(
        11, wraps=betterproto.TYPE_STRING
    )
    state_hvac_operation_mode_ui: Optional[str] = betterproto.message_field(
        12, wraps=betterproto.TYPE_STRING
    )
    state_hvac_fan_mode_is_always_on: Optional[bool] = betterproto.message_field(
        13, wraps=betterproto.TYPE_BOOL
    )
    hvac_mode: Optional[float] = betterproto.message_field(
        14, wraps=betterproto.TYPE_FLOAT
    )
    state_hvac_cooler_is_on_num: Optional[float] = betterproto.message_field(
        15, wraps=betterproto.TYPE_FLOAT
    )
    state_hvac_operation_mode_num: Optional[float] = betterproto.message_field(
        16, wraps=betterproto.TYPE_FLOAT
    )
    temperature_sensor_count_num: Optional[float] = betterproto.message_field(
        17, wraps=betterproto.TYPE_FLOAT
    )
    state_hvac_operation_mode_is_heat: Optional[bool] = betterproto.message_field(
        18, wraps=betterproto.TYPE_BOOL
    )
    state_setpoint_heat: Optional[float] = betterproto.message_field(
        19, wraps=betterproto.TYPE_FLOAT
    )
    state_hvac_operation_mode_is_off_num: Optional[float] = betterproto.message_field(
        20, wraps=betterproto.TYPE_FLOAT
    )
    name: Optional[str] = betterproto.message_field(21, wraps=betterproto.TYPE_STRING)
    state_temperature_input1: Optional[float] = betterproto.message_field(
        22, wraps=betterproto.TYPE_FLOAT
    )
    humidifier_is_on_num: Optional[float] = betterproto.message_field(
        23, wraps=betterproto.TYPE_FLOAT
    )
    state_hvac_fan_mode_is_auto: Optional[bool] = betterproto.message_field(
        24, wraps=betterproto.TYPE_BOOL
    )
    supports_all_off_num: Optional[float] = betterproto.message_field(
        25, wraps=betterproto.TYPE_FLOAT
    )
    enabled_num: Optional[float] = betterproto.message_field(
        26, wraps=betterproto.TYPE_FLOAT
    )
    fan_is_on_num: Optional[float] = betterproto.message_field(
        27, wraps=betterproto.TYPE_FLOAT
    )
    state_hvac_operation_mode_is_program_heat: Optional[
        bool
    ] = betterproto.message_field(28, wraps=betterproto.TYPE_BOOL)
    configured: Optional[bool] = betterproto.message_field(
        29, wraps=betterproto.TYPE_BOOL
    )
    state_hvac_operation_mode_is_heat_num: Optional[float] = betterproto.message_field(
        30, wraps=betterproto.TYPE_FLOAT
    )
    remote_display_num: Optional[float] = betterproto.message_field(
        31, wraps=betterproto.TYPE_FLOAT
    )
    button_group_count_num: Optional[float] = betterproto.message_field(
        32, wraps=betterproto.TYPE_FLOAT
    )
    cool_is_on_num: Optional[float] = betterproto.message_field(
        33, wraps=betterproto.TYPE_FLOAT
    )
    state_hvac_operation_mode_is_program_cool: Optional[
        bool
    ] = betterproto.message_field(34, wraps=betterproto.TYPE_BOOL)
    display_state_val_ui: Optional[str] = betterproto.message_field(
        35, wraps=betterproto.TYPE_STRING
    )
    hvac_mode_num: Optional[float] = betterproto.message_field(
        36, wraps=betterproto.TYPE_FLOAT
    )
    cool_setpoint: Optional[float] = betterproto.message_field(
        37, wraps=betterproto.TYPE_FLOAT
    )
    state_hvac_dehumidifier_is_on: Optional[bool] = betterproto.message_field(
        38, wraps=betterproto.TYPE_BOOL
    )
    state_hvac_operation_mode_is_program_auto: Optional[
        bool
    ] = betterproto.message_field(39, wraps=betterproto.TYPE_BOOL)
    version: Optional[float] = betterproto.message_field(
        40, wraps=betterproto.TYPE_FLOAT
    )
    display_state_id: Optional[str] = betterproto.message_field(
        41, wraps=betterproto.TYPE_STRING
    )
    fan_mode_num: Optional[float] = betterproto.message_field(
        42, wraps=betterproto.TYPE_FLOAT
    )
    state_hvac_fan_mode: Optional[float] = betterproto.message_field(
        43, wraps=betterproto.TYPE_FLOAT
    )
    supports_hvac_fan_mode: Optional[bool] = betterproto.message_field(
        44, wraps=betterproto.TYPE_BOOL
    )
    supports_all_lights_on_off_num: Optional[float] = betterproto.message_field(
        45, wraps=betterproto.TYPE_FLOAT
    )
    humidity_sensor_count_num: Optional[float] = betterproto.message_field(
        46, wraps=betterproto.TYPE_FLOAT
    )
    address: Optional[str] = betterproto.message_field(
        47, wraps=betterproto.TYPE_STRING
    )
    id_num: Optional[float] = betterproto.message_field(
        48, wraps=betterproto.TYPE_FLOAT
    )
    supports_cool_setpoint: Optional[bool] = betterproto.message_field(
        49, wraps=betterproto.TYPE_BOOL
    )
    state_hvac_fan_mode_num: Optional[float] = betterproto.message_field(
        50, wraps=betterproto.TYPE_FLOAT
    )
    last_changed: Optional[float] = betterproto.message_field(
        51, wraps=betterproto.TYPE_FLOAT
    )
    version_num: Optional[float] = betterproto.message_field(
        52, wraps=betterproto.TYPE_FLOAT
    )
    display_state_image_sel: Optional[str] = betterproto.message_field(
        53, wraps=betterproto.TYPE_STRING
    )
    state_hvac_fan_mode_is_auto_num: Optional[float] = betterproto.message_field(
        54, wraps=betterproto.TYPE_FLOAT
    )
    display_state_val_raw: Optional[str] = betterproto.message_field(
        55, wraps=betterproto.TYPE_STRING
    )
    fan_is_on: Optional[bool] = betterproto.message_field(
        56, wraps=betterproto.TYPE_BOOL
    )
    humidity_sensor_count: Optional[float] = betterproto.message_field(
        57, wraps=betterproto.TYPE_FLOAT
    )
    state_humidity_inputs_all_num: Optional[float] = betterproto.message_field(
        58, wraps=betterproto.TYPE_FLOAT
    )
    state_temperature_inputs_all: Optional[str] = betterproto.message_field(
        59, wraps=betterproto.TYPE_STRING
    )
    sub_model: Optional[str] = betterproto.message_field(
        60, wraps=betterproto.TYPE_STRING
    )
    supports_all_off: Optional[bool] = betterproto.message_field(
        61, wraps=betterproto.TYPE_BOOL
    )
    state_hvac_operation_mode_is_program_auto_num: Optional[
        float
    ] = betterproto.message_field(62, wraps=betterproto.TYPE_FLOAT)
    state_hvac_operation_mode: Optional[float] = betterproto.message_field(
        63, wraps=betterproto.TYPE_FLOAT
    )
    temperature_sensor_count: Optional[float] = betterproto.message_field(
        64, wraps=betterproto.TYPE_FLOAT
    )
    supports_status_request: Optional[bool] = betterproto.message_field(
        65, wraps=betterproto.TYPE_BOOL
    )
    supports_heat_setpoint_num: Optional[float] = betterproto.message_field(
        66, wraps=betterproto.TYPE_FLOAT
    )
    supports_hvac_fan_mode_num: Optional[float] = betterproto.message_field(
        67, wraps=betterproto.TYPE_FLOAT
    )
    state_hvac_fan_mode_is_always_on_num: Optional[float] = betterproto.message_field(
        68, wraps=betterproto.TYPE_FLOAT
    )
    heat_is_on_num: Optional[float] = betterproto.message_field(
        69, wraps=betterproto.TYPE_FLOAT
    )
    folder_id: Optional[float] = betterproto.message_field(
        70, wraps=betterproto.TYPE_FLOAT
    )
    supports_heat_setpoint: Optional[bool] = betterproto.message_field(
        71, wraps=betterproto.TYPE_BOOL
    )
    humidifier_is_on: Optional[bool] = betterproto.message_field(
        72, wraps=betterproto.TYPE_BOOL
    )
    supports_status_request_num: Optional[float] = betterproto.message_field(
        73, wraps=betterproto.TYPE_FLOAT
    )
    enabled: Optional[bool] = betterproto.message_field(74, wraps=betterproto.TYPE_BOOL)
    state_hvac_fan_mode_ui: Optional[str] = betterproto.message_field(
        75, wraps=betterproto.TYPE_STRING
    )
    remote_display: Optional[bool] = betterproto.message_field(
        76, wraps=betterproto.TYPE_BOOL
    )
    supports_all_lights_on_off: Optional[bool] = betterproto.message_field(
        77, wraps=betterproto.TYPE_BOOL
    )
    state_hvac_humidifier_is_on_num: Optional[float] = betterproto.message_field(
        78, wraps=betterproto.TYPE_FLOAT
    )
    state_hvac_operation_mode_is_cool_num: Optional[float] = betterproto.message_field(
        79, wraps=betterproto.TYPE_FLOAT
    )
    state_hvac_humidifier_is_on: Optional[bool] = betterproto.message_field(
        80, wraps=betterproto.TYPE_BOOL
    )
    state_hvac_operation_mode_is_program_cool_num: Optional[
        float
    ] = betterproto.message_field(81, wraps=betterproto.TYPE_FLOAT)
    heat_is_on: Optional[bool] = betterproto.message_field(
        82, wraps=betterproto.TYPE_BOOL
    )
    state_hvac_operation_mode_is_cool: Optional[bool] = betterproto.message_field(
        83, wraps=betterproto.TYPE_BOOL
    )
    button_group_count: Optional[float] = betterproto.message_field(
        84, wraps=betterproto.TYPE_FLOAT
    )
    id: Optional[float] = betterproto.message_field(85, wraps=betterproto.TYPE_FLOAT)
    state_hvac_operation_mode_is_auto: Optional[bool] = betterproto.message_field(
        86, wraps=betterproto.TYPE_BOOL
    )
    state_setpoint_cool: Optional[float] = betterproto.message_field(
        87, wraps=betterproto.TYPE_FLOAT
    )
    device_type_id: Optional[str] = betterproto.message_field(
        88, wraps=betterproto.TYPE_STRING
    )
    configured_num: Optional[float] = betterproto.message_field(
        89, wraps=betterproto.TYPE_FLOAT
    )
    dehumidifier_is_on: Optional[bool] = betterproto.message_field(
        90, wraps=betterproto.TYPE_BOOL
    )
    state_hvac_operation_mode_is_auto_num: Optional[float] = betterproto.message_field(
        91, wraps=betterproto.TYPE_FLOAT
    )
    folder_id_num: Optional[float] = betterproto.message_field(
        92, wraps=betterproto.TYPE_FLOAT
    )
    supports_hvac_operation_mode: Optional[bool] = betterproto.message_field(
        93, wraps=betterproto.TYPE_BOOL
    )
    state_hvac_heater_is_on_num: Optional[float] = betterproto.message_field(
        94, wraps=betterproto.TYPE_FLOAT
    )
    description: Optional[str] = betterproto.message_field(
        95, wraps=betterproto.TYPE_STRING
    )
    state_temperature_inputs_all_num: Optional[float] = betterproto.message_field(
        96, wraps=betterproto.TYPE_FLOAT
    )
    supports_hvac_operation_mode_num: Optional[float] = betterproto.message_field(
        97, wraps=betterproto.TYPE_FLOAT
    )
    state_hvac_operation_mode_is_program_heat_num: Optional[
        float
    ] = betterproto.message_field(98, wraps=betterproto.TYPE_FLOAT)
    cool_is_on: Optional[bool] = betterproto.message_field(
        99, wraps=betterproto.TYPE_BOOL
    )
    heat_setpoint: Optional[float] = betterproto.message_field(
        100, wraps=betterproto.TYPE_FLOAT
    )
    fan_mode: Optional[float] = betterproto.message_field(
        101, wraps=betterproto.TYPE_FLOAT
    )
    state_hvac_cooler_is_on: Optional[bool] = betterproto.message_field(
        102, wraps=betterproto.TYPE_BOOL
    )
    state_humidity_input1: Optional[float] = betterproto.message_field(
        103, wraps=betterproto.TYPE_FLOAT
    )
    state_hvac_fan_is_on_num: Optional[float] = betterproto.message_field(
        104, wraps=betterproto.TYPE_FLOAT
    )
    model: Optional[str] = betterproto.message_field(105, wraps=betterproto.TYPE_STRING)


@dataclass
class BinarySwitchFields(betterproto.Message):
    sub_model: Optional[str] = betterproto.message_field(
        1, wraps=betterproto.TYPE_STRING
    )
    protocol: Optional[str] = betterproto.message_field(
        2, wraps=betterproto.TYPE_STRING
    )
    configured: Optional[bool] = betterproto.message_field(
        3, wraps=betterproto.TYPE_BOOL
    )
    button_configured_count_num: Optional[float] = betterproto.message_field(
        4, wraps=betterproto.TYPE_FLOAT
    )
    plugin_id: Optional[str] = betterproto.message_field(
        5, wraps=betterproto.TYPE_STRING
    )
    button_group_count_num: Optional[float] = betterproto.message_field(
        6, wraps=betterproto.TYPE_FLOAT
    )
    last_successful_comm: Optional[float] = betterproto.message_field(
        7, wraps=betterproto.TYPE_FLOAT
    )
    button_group_count: Optional[float] = betterproto.message_field(
        8, wraps=betterproto.TYPE_FLOAT
    )
    id: Optional[float] = betterproto.message_field(9, wraps=betterproto.TYPE_FLOAT)
    on_state_num: Optional[float] = betterproto.message_field(
        10, wraps=betterproto.TYPE_FLOAT
    )
    supports_all_off: Optional[bool] = betterproto.message_field(
        11, wraps=betterproto.TYPE_BOOL
    )
    error_state: Optional[str] = betterproto.message_field(
        12, wraps=betterproto.TYPE_STRING
    )
    remote_display: Optional[bool] = betterproto.message_field(
        13, wraps=betterproto.TYPE_BOOL
    )
    configured_num: Optional[float] = betterproto.message_field(
        14, wraps=betterproto.TYPE_FLOAT
    )
    supports_all_lights_on_off: Optional[bool] = betterproto.message_field(
        15, wraps=betterproto.TYPE_BOOL
    )
    display_state_val_ui: Optional[str] = betterproto.message_field(
        16, wraps=betterproto.TYPE_STRING
    )
    version: Optional[float] = betterproto.message_field(
        17, wraps=betterproto.TYPE_FLOAT
    )
    display_state_id: Optional[str] = betterproto.message_field(
        18, wraps=betterproto.TYPE_STRING
    )
    state_on_off_state: Optional[bool] = betterproto.message_field(
        19, wraps=betterproto.TYPE_BOOL
    )
    supports_status_request: Optional[bool] = betterproto.message_field(
        20, wraps=betterproto.TYPE_BOOL
    )
    folder_id_num: Optional[float] = betterproto.message_field(
        21, wraps=betterproto.TYPE_FLOAT
    )
    remote_display_num: Optional[float] = betterproto.message_field(
        22, wraps=betterproto.TYPE_FLOAT
    )
    description: Optional[str] = betterproto.message_field(
        23, wraps=betterproto.TYPE_STRING
    )
    on_state: Optional[bool] = betterproto.message_field(
        24, wraps=betterproto.TYPE_BOOL
    )
    supports_all_lights_on_off_num: Optional[float] = betterproto.message_field(
        25, wraps=betterproto.TYPE_FLOAT
    )
    address: Optional[str] = betterproto.message_field(
        26, wraps=betterproto.TYPE_STRING
    )
    folder_id: Optional[float] = betterproto.message_field(
        27, wraps=betterproto.TYPE_FLOAT
    )
    id_num: Optional[float] = betterproto.message_field(
        28, wraps=betterproto.TYPE_FLOAT
    )
    button_configured_count: Optional[float] = betterproto.message_field(
        29, wraps=betterproto.TYPE_FLOAT
    )
    name: Optional[str] = betterproto.message_field(30, wraps=betterproto.TYPE_STRING)
    supports_status_request_num: Optional[float] = betterproto.message_field(
        31, wraps=betterproto.TYPE_FLOAT
    )
    last_changed: Optional[float] = betterproto.message_field(
        32, wraps=betterproto.TYPE_FLOAT
    )
    state_on_off_state_num: Optional[float] = betterproto.message_field(
        33, wraps=betterproto.TYPE_FLOAT
    )
    version_num: Optional[float] = betterproto.message_field(
        34, wraps=betterproto.TYPE_FLOAT
    )
    enabled: Optional[bool] = betterproto.message_field(35, wraps=betterproto.TYPE_BOOL)
    supports_all_off_num: Optional[float] = betterproto.message_field(
        36, wraps=betterproto.TYPE_FLOAT
    )
    device_type_id: Optional[str] = betterproto.message_field(
        37, wraps=betterproto.TYPE_STRING
    )
    enabled_num: Optional[float] = betterproto.message_field(
        38, wraps=betterproto.TYPE_FLOAT
    )
    display_state_image_sel: Optional[str] = betterproto.message_field(
        39, wraps=betterproto.TYPE_STRING
    )
    display_state_val_raw: Optional[str] = betterproto.message_field(
        40, wraps=betterproto.TYPE_STRING
    )
    model: Optional[str] = betterproto.message_field(41, wraps=betterproto.TYPE_STRING)


@dataclass
class SecurityFields(betterproto.Message):
    sub_model: Optional[str] = betterproto.message_field(
        1, wraps=betterproto.TYPE_STRING
    )
    protocol: Optional[str] = betterproto.message_field(
        2, wraps=betterproto.TYPE_STRING
    )
    state_bypass_nobypass: Optional[bool] = betterproto.message_field(
        3, wraps=betterproto.TYPE_BOOL
    )
    configured: Optional[bool] = betterproto.message_field(
        4, wraps=betterproto.TYPE_BOOL
    )
    state_state_closed: Optional[bool] = betterproto.message_field(
        5, wraps=betterproto.TYPE_BOOL
    )
    state_state: Optional[str] = betterproto.message_field(
        6, wraps=betterproto.TYPE_STRING
    )
    state_state_tripped_num: Optional[float] = betterproto.message_field(
        7, wraps=betterproto.TYPE_FLOAT
    )
    plugin_id: Optional[str] = betterproto.message_field(
        8, wraps=betterproto.TYPE_STRING
    )
    button_group_count_num: Optional[float] = betterproto.message_field(
        9, wraps=betterproto.TYPE_FLOAT
    )
    last_successful_comm: Optional[float] = betterproto.message_field(
        10, wraps=betterproto.TYPE_FLOAT
    )
    button_group_count: Optional[float] = betterproto.message_field(
        11, wraps=betterproto.TYPE_FLOAT
    )
    id: Optional[float] = betterproto.message_field(12, wraps=betterproto.TYPE_FLOAT)
    state_bypass_nobypass_num: Optional[float] = betterproto.message_field(
        13, wraps=betterproto.TYPE_FLOAT
    )
    supports_all_off: Optional[bool] = betterproto.message_field(
        14, wraps=betterproto.TYPE_BOOL
    )
    error_state: Optional[str] = betterproto.message_field(
        15, wraps=betterproto.TYPE_STRING
    )
    state_state_open_num: Optional[float] = betterproto.message_field(
        16, wraps=betterproto.TYPE_FLOAT
    )
    remote_display: Optional[bool] = betterproto.message_field(
        17, wraps=betterproto.TYPE_BOOL
    )
    configured_num: Optional[float] = betterproto.message_field(
        18, wraps=betterproto.TYPE_FLOAT
    )
    supports_all_lights_on_off: Optional[bool] = betterproto.message_field(
        19, wraps=betterproto.TYPE_BOOL
    )
    display_state_val_ui: Optional[str] = betterproto.message_field(
        20, wraps=betterproto.TYPE_STRING
    )
    display_state_id: Optional[str] = betterproto.message_field(
        21, wraps=betterproto.TYPE_STRING
    )
    state__last_changed_timer: Optional[float] = betterproto.message_field(
        22, wraps=betterproto.TYPE_FLOAT
    )
    state_state_tripped: Optional[bool] = betterproto.message_field(
        23, wraps=betterproto.TYPE_BOOL
    )
    supports_status_request: Optional[bool] = betterproto.message_field(
        24, wraps=betterproto.TYPE_BOOL
    )
    folder_id_num: Optional[float] = betterproto.message_field(
        25, wraps=betterproto.TYPE_FLOAT
    )
    remote_display_num: Optional[float] = betterproto.message_field(
        26, wraps=betterproto.TYPE_FLOAT
    )
    description: Optional[str] = betterproto.message_field(
        27, wraps=betterproto.TYPE_STRING
    )
    state_bypass_bypassed_num: Optional[float] = betterproto.message_field(
        28, wraps=betterproto.TYPE_FLOAT
    )
    state_state_open: Optional[bool] = betterproto.message_field(
        29, wraps=betterproto.TYPE_BOOL
    )
    state__last_changed_short: Optional[str] = betterproto.message_field(
        30, wraps=betterproto.TYPE_STRING
    )
    supports_all_lights_on_off_num: Optional[float] = betterproto.message_field(
        31, wraps=betterproto.TYPE_FLOAT
    )
    address: Optional[str] = betterproto.message_field(
        32, wraps=betterproto.TYPE_STRING
    )
    folder_id: Optional[float] = betterproto.message_field(
        33, wraps=betterproto.TYPE_FLOAT
    )
    id_num: Optional[float] = betterproto.message_field(
        34, wraps=betterproto.TYPE_FLOAT
    )
    state__last_changed_timer_num: Optional[float] = betterproto.message_field(
        35, wraps=betterproto.TYPE_FLOAT
    )
    state_state_closed_num: Optional[float] = betterproto.message_field(
        36, wraps=betterproto.TYPE_FLOAT
    )
    name: Optional[str] = betterproto.message_field(37, wraps=betterproto.TYPE_STRING)
    supports_status_request_num: Optional[float] = betterproto.message_field(
        38, wraps=betterproto.TYPE_FLOAT
    )
    last_changed: Optional[float] = betterproto.message_field(
        39, wraps=betterproto.TYPE_FLOAT
    )
    state_bypass_bypassed: Optional[bool] = betterproto.message_field(
        40, wraps=betterproto.TYPE_BOOL
    )
    enabled: Optional[bool] = betterproto.message_field(41, wraps=betterproto.TYPE_BOOL)
    state_bypass: Optional[str] = betterproto.message_field(
        42, wraps=betterproto.TYPE_STRING
    )
    supports_all_off_num: Optional[float] = betterproto.message_field(
        43, wraps=betterproto.TYPE_FLOAT
    )
    device_type_id: Optional[str] = betterproto.message_field(
        44, wraps=betterproto.TYPE_STRING
    )
    enabled_num: Optional[float] = betterproto.message_field(
        45, wraps=betterproto.TYPE_FLOAT
    )
    display_state_image_sel: Optional[str] = betterproto.message_field(
        46, wraps=betterproto.TYPE_STRING
    )
    display_state_val_raw: Optional[str] = betterproto.message_field(
        47, wraps=betterproto.TYPE_STRING
    )
    model: Optional[str] = betterproto.message_field(48, wraps=betterproto.TYPE_STRING)


@dataclass
class DimmerSwitchFields(betterproto.Message):
    sub_model: Optional[str] = betterproto.message_field(
        1, wraps=betterproto.TYPE_STRING
    )
    supports_r_g_band_white_simultaneously_num: Optional[
        float
    ] = betterproto.message_field(2, wraps=betterproto.TYPE_FLOAT)
    protocol: Optional[str] = betterproto.message_field(
        3, wraps=betterproto.TYPE_STRING
    )
    default_brightness_num: Optional[float] = betterproto.message_field(
        4, wraps=betterproto.TYPE_FLOAT
    )
    configured: Optional[bool] = betterproto.message_field(
        5, wraps=betterproto.TYPE_BOOL
    )
    address: Optional[str] = betterproto.message_field(6, wraps=betterproto.TYPE_STRING)
    button_configured_count_num: Optional[float] = betterproto.message_field(
        7, wraps=betterproto.TYPE_FLOAT
    )
    plugin_id: Optional[str] = betterproto.message_field(
        8, wraps=betterproto.TYPE_STRING
    )
    remote_display_num: Optional[float] = betterproto.message_field(
        9, wraps=betterproto.TYPE_FLOAT
    )
    button_group_count_num: Optional[float] = betterproto.message_field(
        10, wraps=betterproto.TYPE_FLOAT
    )
    state_on_off_state_num: Optional[float] = betterproto.message_field(
        11, wraps=betterproto.TYPE_FLOAT
    )
    last_successful_comm: Optional[float] = betterproto.message_field(
        12, wraps=betterproto.TYPE_FLOAT
    )
    version_num: Optional[float] = betterproto.message_field(
        13, wraps=betterproto.TYPE_FLOAT
    )
    button_group_count: Optional[float] = betterproto.message_field(
        14, wraps=betterproto.TYPE_FLOAT
    )
    supports_white_temperature: Optional[bool] = betterproto.message_field(
        15, wraps=betterproto.TYPE_BOOL
    )
    supports_two_white_levels_num: Optional[float] = betterproto.message_field(
        16, wraps=betterproto.TYPE_FLOAT
    )
    display_state_val_ui: Optional[str] = betterproto.message_field(
        17, wraps=betterproto.TYPE_STRING
    )
    on_state_num: Optional[float] = betterproto.message_field(
        18, wraps=betterproto.TYPE_FLOAT
    )
    supports_all_off: Optional[bool] = betterproto.message_field(
        19, wraps=betterproto.TYPE_BOOL
    )
    error_state: Optional[str] = betterproto.message_field(
        20, wraps=betterproto.TYPE_STRING
    )
    supports_color_num: Optional[float] = betterproto.message_field(
        21, wraps=betterproto.TYPE_FLOAT
    )
    remote_display: Optional[bool] = betterproto.message_field(
        22, wraps=betterproto.TYPE_BOOL
    )
    configured_num: Optional[float] = betterproto.message_field(
        23, wraps=betterproto.TYPE_FLOAT
    )
    state_brightness_level: Optional[float] = betterproto.message_field(
        24, wraps=betterproto.TYPE_FLOAT
    )
    supports_all_lights_on_off: Optional[bool] = betterproto.message_field(
        25, wraps=betterproto.TYPE_BOOL
    )
    id: Optional[float] = betterproto.message_field(26, wraps=betterproto.TYPE_FLOAT)
    supports_white: Optional[bool] = betterproto.message_field(
        27, wraps=betterproto.TYPE_BOOL
    )
    state_brightness_level_num: Optional[float] = betterproto.message_field(
        28, wraps=betterproto.TYPE_FLOAT
    )
    version: Optional[float] = betterproto.message_field(
        29, wraps=betterproto.TYPE_FLOAT
    )
    display_state_id: Optional[str] = betterproto.message_field(
        30, wraps=betterproto.TYPE_STRING
    )
    state_on_off_state: Optional[bool] = betterproto.message_field(
        31, wraps=betterproto.TYPE_BOOL
    )
    supports_color: Optional[bool] = betterproto.message_field(
        32, wraps=betterproto.TYPE_BOOL
    )
    brightness_num: Optional[float] = betterproto.message_field(
        33, wraps=betterproto.TYPE_FLOAT
    )
    supports_r_g_band_white_simultaneously: Optional[bool] = betterproto.message_field(
        34, wraps=betterproto.TYPE_BOOL
    )
    on_brightens_to_last: Optional[bool] = betterproto.message_field(
        35, wraps=betterproto.TYPE_BOOL
    )
    description: Optional[str] = betterproto.message_field(
        36, wraps=betterproto.TYPE_STRING
    )
    id_num: Optional[float] = betterproto.message_field(
        37, wraps=betterproto.TYPE_FLOAT
    )
    on_state: Optional[bool] = betterproto.message_field(
        38, wraps=betterproto.TYPE_BOOL
    )
    on_brightens_to_default_toggle: Optional[bool] = betterproto.message_field(
        39, wraps=betterproto.TYPE_BOOL
    )
    supports_all_lights_on_off_num: Optional[float] = betterproto.message_field(
        40, wraps=betterproto.TYPE_FLOAT
    )
    supports_r_g_b_num: Optional[float] = betterproto.message_field(
        41, wraps=betterproto.TYPE_FLOAT
    )
    supports_r_g_b: Optional[bool] = betterproto.message_field(
        42, wraps=betterproto.TYPE_BOOL
    )
    default_brightness: Optional[float] = betterproto.message_field(
        43, wraps=betterproto.TYPE_FLOAT
    )
    folder_id: Optional[float] = betterproto.message_field(
        44, wraps=betterproto.TYPE_FLOAT
    )
    supports_two_white_levels: Optional[bool] = betterproto.message_field(
        45, wraps=betterproto.TYPE_BOOL
    )
    supports_white_temperature_num: Optional[float] = betterproto.message_field(
        46, wraps=betterproto.TYPE_FLOAT
    )
    supports_white_num: Optional[float] = betterproto.message_field(
        47, wraps=betterproto.TYPE_FLOAT
    )
    button_configured_count: Optional[float] = betterproto.message_field(
        48, wraps=betterproto.TYPE_FLOAT
    )
    name: Optional[str] = betterproto.message_field(49, wraps=betterproto.TYPE_STRING)
    supports_status_request_num: Optional[float] = betterproto.message_field(
        50, wraps=betterproto.TYPE_FLOAT
    )
    brightness: Optional[float] = betterproto.message_field(
        51, wraps=betterproto.TYPE_FLOAT
    )
    supports_two_white_levels_simultaneously_num: Optional[
        float
    ] = betterproto.message_field(52, wraps=betterproto.TYPE_FLOAT)
    on_brightens_to_default_toggle_num: Optional[float] = betterproto.message_field(
        53, wraps=betterproto.TYPE_FLOAT
    )
    last_changed: Optional[float] = betterproto.message_field(
        54, wraps=betterproto.TYPE_FLOAT
    )
    enabled: Optional[bool] = betterproto.message_field(55, wraps=betterproto.TYPE_BOOL)
    on_brightens_to_last_num: Optional[float] = betterproto.message_field(
        56, wraps=betterproto.TYPE_FLOAT
    )
    supports_two_white_levels_simultaneously: Optional[
        bool
    ] = betterproto.message_field(57, wraps=betterproto.TYPE_BOOL)
    folder_id_num: Optional[float] = betterproto.message_field(
        58, wraps=betterproto.TYPE_FLOAT
    )
    supports_all_off_num: Optional[float] = betterproto.message_field(
        59, wraps=betterproto.TYPE_FLOAT
    )
    device_type_id: Optional[str] = betterproto.message_field(
        60, wraps=betterproto.TYPE_STRING
    )
    enabled_num: Optional[float] = betterproto.message_field(
        61, wraps=betterproto.TYPE_FLOAT
    )
    display_state_image_sel: Optional[str] = betterproto.message_field(
        62, wraps=betterproto.TYPE_STRING
    )
    display_state_val_raw: Optional[str] = betterproto.message_field(
        63, wraps=betterproto.TYPE_STRING
    )
    supports_status_request: Optional[bool] = betterproto.message_field(
        64, wraps=betterproto.TYPE_BOOL
    )
    model: Optional[str] = betterproto.message_field(65, wraps=betterproto.TYPE_STRING)


@dataclass
class GenericFields(betterproto.Message):
    last_successful_comm: Optional[float] = betterproto.message_field(
        1, wraps=betterproto.TYPE_FLOAT
    )
    id: Optional[float] = betterproto.message_field(2, wraps=betterproto.TYPE_FLOAT)
    name: Optional[str] = betterproto.message_field(3, wraps=betterproto.TYPE_STRING)
    last_changed: Optional[float] = betterproto.message_field(
        4, wraps=betterproto.TYPE_FLOAT
    )


@dataclass
class IndigoUnknownMessage(betterproto.Message):
    measurement: Optional[str] = betterproto.message_field(
        1, wraps=betterproto.TYPE_STRING
    )
    time: datetime = betterproto.message_field(2)
    tags: "IndigoTags" = betterproto.message_field(4)
    binary: "BinarySwitchFields" = betterproto.message_field(11, group="fields")
    dimmer: "DimmerSwitchFields" = betterproto.message_field(12, group="fields")
    hvac: "HvacFields" = betterproto.message_field(13, group="fields")
    security: "SecurityFields" = betterproto.message_field(14, group="fields")
    generic: "GenericFields" = betterproto.message_field(15, group="fields")


@dataclass
class SubscribeArgs(betterproto.Message):
    multicast_port: int = betterproto.uint32_field(1)


class TranslatorStub(betterproto.ServiceStub):
    """A service that translates raw JSON messages to the above structures"""

    async def subscribe(
        self, *, multicast_port: int = 0
    ) -> AsyncGenerator[IndigoUnknownMessage, None]:
        """Subscribe to ongoing message updates"""

        request = SubscribeArgs()
        request.multicast_port = multicast_port

        async for response in self._unary_stream(
            "/indigo.Translator/Subscribe", request, IndigoUnknownMessage,
        ):
            yield response
