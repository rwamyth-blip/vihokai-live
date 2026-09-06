import json
from urllib.parse import urlencode

from fastapi import APIRouter, HTTPException
from fastapi.responses import RedirectResponse

from auth import (
    FRONTEND_URL,
    JWT_EXPIRY,
    create_jwt,
    exchange_code_for_token,
    get_user_info,
    save_or_get_user,
)

router = APIRouter()


@router.get("/api/auth/google/callback")
async def google_callback(code: str):
    try:
        token_data = await exchange_code_for_token(code)
        user_info = await get_user_info(token_data["access_token"])
        db_user = save_or_get_user(user_info)
        if not db_user or not db_user.get("id") or not db_user.get("email"):
            raise HTTPException(status_code=502, detail="User record is incomplete")

        app_token = create_jwt(
            user_id=str(db_user["id"]),
            email=db_user["email"],
            name=db_user.get("name") or user_info.get("name", ""),
        )
        callback_url = f"{FRONTEND_URL}/auth/callback?" + urlencode({
            "token": app_token,
            "user": json.dumps(db_user, ensure_ascii=False),
        })
        return RedirectResponse(url=callback_url, status_code=303)
    except HTTPException:
        raise
    except Exception as error:
        print(f"Google OAuth callback failed: {type(error).__name__}: {error}")
        raise HTTPException(
            status_code=502,
            detail="Google login could not be completed. Check backend logs.",
        ) from error