from __future__ import annotations

import json
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


class MiniProgramDataTests(unittest.TestCase):
    def payloads(self) -> tuple[dict, dict]:
        bundle = ROOT / "wechat-miniprogram" / "miniprogram" / "data" / "rankings.js"
        content = bundle.read_text(encoding="utf-8")
        bundled = json.loads(content.split("module.exports = ", 1)[1].rstrip(";\n"))
        public = json.loads((ROOT / "data" / "miniprogram" / "latest.json").read_text(encoding="utf-8"))
        return bundled, public

    def test_bundle_is_valid_and_contains_all_modules(self) -> None:
        payload, _ = self.payloads()
        self.assertEqual(18, payload["module_count"])
        self.assertEqual(payload["module_count"], len(payload["modules"]))
        for module in payload["modules"]:
            self.assertLessEqual(len(module["composite"]), 5)
            self.assertLessEqual(len(module["momentum"]), 5)
            self.assertTrue(module["color"].startswith("#"))

    def test_public_payload_matches_bundled_fallback(self) -> None:
        bundled, public = self.payloads()
        self.assertEqual(bundled, public)

    def test_mini_program_fetches_pages_payload(self) -> None:
        app_js = (ROOT / "wechat-miniprogram" / "miniprogram" / "app.js").read_text(encoding="utf-8")
        self.assertIn("https://yuxiaoyi24.github.io/ai-agent-open-source-ranking/data/latest.json", app_js)
        self.assertIn("wx.request", app_js)
        self.assertIn("wx.setStorageSync", app_js)

    def test_project_config_uses_existing_appid(self) -> None:
        config = json.loads((ROOT / "wechat-miniprogram" / "project.config.json").read_text(encoding="utf-8"))
        self.assertEqual("wxa5fdbcf1f1f80135", config["appid"])
        self.assertEqual("miniprogram/", config["miniprogramRoot"])
