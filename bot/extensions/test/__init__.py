from bot.extensions.test.commands import Test

async def setup(bot):
    await bot.add_cog(Test(bot))
