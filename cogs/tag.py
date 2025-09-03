from discord.ext import commands
from config import SERVER_ID, VERIFICATED_ID

class AutoRole(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_member_join(self, member):
        if member.guild.id == SERVER_ID:
            role = member.guild.get_role(VERIFICATED_ID)
            if role:
                await member.add_roles(role)
                print(f"👤 {member} entrou no servidor e recebeu o cargo {role.name}")

async def setup(bot):
    await bot.add_cog(AutoRole(bot))